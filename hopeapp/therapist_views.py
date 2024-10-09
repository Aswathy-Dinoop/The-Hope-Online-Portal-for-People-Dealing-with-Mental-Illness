from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage
from hopeapp.models import BookedTherapists, Problems, Registration, TherapistRegistration, Add_Category, PostDepressionSolutions
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class index(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/index.html'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = TherapistRegistration.objects.get(user_id=id1)
        context['profile'] = pro
        return context


class UpdateProfile(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/upd_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = TherapistRegistration.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        phone = request.POST['phone']
        location = request.POST['location']
        about = request.POST['about']
        fees = request.POST['fees']
        hname = request.POST['hname']
        exp= request.POST['exp']
        wtime = request.POST['working-time']
        pincode = request.POST['pincode']
        image = request.FILES['image']
        ob = FileSystemStorage()
        obj = ob.save(image.name, image)
        reg = TherapistRegistration.objects.get(id=id3)  # call the model
        reg.phone = phone
        reg.location = location
        reg.about = about
        reg.fees = fees
        reg.hname = hname
        reg.exp=exp
        reg.wtime=wtime
        reg.pincode = pincode
        reg.image = obj
        reg.save()
        return render(request, 'therapist/index.html', {'message': "Successfully Updated"})


class Post_Depressions(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/post_dep_sol.html'

    def get_context_data(self, **kwargs):
        context = super(Post_Depressions, self).get_context_data(**kwargs)
        pro = Add_Category.objects.all()
        context['cate'] = pro
        return context

    def post(self, request, *args, **kwargs):
        xyz = TherapistRegistration.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        category = request.POST['cate']
        solutions = request.POST['solutions']
        image = request.FILES['image']

        ob = FileSystemStorage()
        obj = ob.save(image.name, image)

        reg = PostDepressionSolutions()  # call the model
        reg.therapy_id = xyz.id
        reg.name = name
        reg.category_id = category
        reg.solutions = solutions
        reg.image = obj
        reg.save()
        return redirect('/therapist')


class ViewDepressions(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/viewdepressions.html'

    def get_context_data(self, **kwargs):
        context = super(ViewDepressions, self).get_context_data(**kwargs)
        abc = TherapistRegistration.objects.get(user_id=self.request.user.id)
        pro = PostDepressionSolutions.objects.filter(therapy_id=abc.id)
        context['depres'] = pro
        return context


class RemoveDep(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        PostDepressionSolutions.objects.get(id=id).delete()
        return redirect('/therapist')


class UpdateDep(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/post_dep_sol.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateDep, self).get_context_data(**kwargs)
        pro = Add_Category.objects.all()
        context['cate'] = pro
        id3 = self.request.GET['id']
        ps = PostDepressionSolutions.objects.get(id=id3)
        context['upd'] = ps
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        # xyz=TherapistRegistration.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        category = request.POST['cate']
        solutions = request.POST['solutions']
        image = request.FILES['image']

        ob = FileSystemStorage()
        obj = ob.save(image.name, image)
        reg = PostDepressionSolutions.objects.get(id=id3)  # call the model
        reg.name = name
        reg.category_id = category
        reg.solutions = solutions
        reg.image = obj
        reg.save()
        # return redirect('/therapist')

        return render(request, 'therapist/index.html', {'message': "Successfully Updated"})


class ViewProblems(LoginRequiredMixin, TemplateView):
    template_name = 'therapist/view_problems.html'

    def get_context_data(self, **kwargs):
        context = super(ViewProblems, self).get_context_data(**kwargs)
        obj = TherapistRegistration.objects.get(user_id=self.request.user.id)

        abc = Problems.objects.filter(therapy_id=obj.id, status='NotReplied')
        context = {
            'problems': abc
        }
        return context

    def post(self, request, *args, **kwargs):
        obj = TherapistRegistration.objects.get(user_id=self.request.user.id)
        id = request.POST['id']
        id2 = request.POST['id2']
        var = Problems.objects.get(id=id2)
        reply = request.POST['reply']
        # abc=Problems.objects.get(id=id2)
        var.status = 'replied'
        var.answer = reply
        var.save()
        return render(request, 'therapist/index.html', {'message': "Replied Successfully "})
    
def view_problem(request):
    obj = TherapistRegistration.objects.get(user_id=request.user.id)

    abc = BookedTherapists.objects.filter(therapy_id=obj.id)
    return render(request,'therapist/view_problems.html',{'abc':abc})