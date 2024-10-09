from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage
from chats.models import Chat
from hopeapp.models import Problems, Registration, PostDepressionSolutions, TherapistRegistration, BookedTherapists ,Rating
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from django.contrib import messages


class index(LoginRequiredMixin, TemplateView):
    template_name = 'user/index.html'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = Registration.objects.get(user_id=id1)
        context['profile'] = pro
        return context


class UpdateProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user/upd_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Registration.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        phone = request.POST['phone']
        location = request.POST['location']
        name = request.POST['name']
        reg = Registration.objects.get(id=id3)  # call the model
        reg.phone = phone
        reg.location = location
        reg.name = name
        reg.save()
        return render(request, 'user/index.html', {'message': "Successfully Updated"})


class ViewAllDepressions(LoginRequiredMixin, TemplateView):
    template_name = 'user/view_depressions.html'

    def get_context_data(self, **kwargs):
        context = super(ViewAllDepressions, self).get_context_data(**kwargs)
        abc = PostDepressionSolutions.objects.all()
        context = {
            'depre': abc
        }
        return context


class SingleDepressions(LoginRequiredMixin, TemplateView):
    template_name = 'user/single_depressions.html'

    def get_context_data(self, **kwargs):
        context = super(SingleDepressions, self).get_context_data(**kwargs)
        id1 = self.request.GET['id']
        view_solu = PostDepressionSolutions.objects.get(id=id1)
        context = {
            'view_solu': view_solu
        }
        return context


class Search(LoginRequiredMixin, TemplateView):
    template_name = 'user/searchtherapist.html'

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        abc = TherapistRegistration.objects.all()
        context = {
            'therapist': abc
        }
        return context

    def post(self, request, *args, **kwargs):
        search = self.request.POST['search']
        therapist = TherapistRegistration.objects.filter(location__icontains=search)

        return render(request, 'user/search.html', {'therapist': therapist})

class feedback(TemplateView):
    template_name='user/feedback.html' 
    def get_context_data(self, **kwargs):
        context = super(feedback, self).get_context_data(**kwargs)
        pro = TherapistRegistration.objects.all()
        context['empl'] = pro
        return context
    

    def post(self, request, *args, **kwargs):
        abc=Registration.objects.get(user_id=self.request.user.id)

        star = request.POST['star']
        print('asdf',star)
        comment = request.POST['comment']
        employee=request.POST['empl']
        gg=TherapistRegistration.objects.get(id=employee)
        # therapy=gg.servicer_id
        reg = Rating()
        reg.star = star
        reg.comment=comment
        # reg.provider_id=provider
        reg.user_id=abc.id
        reg.therapist_id=employee
        reg.status='FeedBack Added'
        reg.save()
        return redirect('/user')
class SingleTherapists(LoginRequiredMixin, TemplateView):
    template_name = 'user/singletherapy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        therapist_id = self.request.GET.get('id')
        if therapist_id:
            therapist = TherapistRegistration.objects.get(id=therapist_id)
            context['view'] = therapist
        return context


    # def post(self, request, *args, **kwargs):
    #     user_id = self.request.user.id
    #     therapist_id = self.request.GET.get('id')
    #     if therapist_id:
    #         # Fetching user registration
    #         user_registration = Registration.objects.get(user_id=user_id)

    #         # Creating booked therapy instance
    #         booked_therapy = BookedTherapists()
    #         booked_therapy.therapy_id = therapist_id
    #         booked_therapy.user_id = user_registration.id
    #         booked_therapy.status = 'Paid'
    #         booked_therapy.save()
    #         booked_therapy.payment_date = datetime.now().date()
    #         expiry_date = booked_therapy.payment_date + timedelta(days=15)
    #         return redirect('user:payment')
    #     # Handle error if therapist id is not provided


class payment(LoginRequiredMixin, TemplateView):
    template_name = "user/payment.html"


# def get_context_data(self, **kwargs):
#     context = super(payment, self).get_context_data(**kwargs)
#     id = self.request.GET['id']

#     if BookedTherapists.objects.filter(therapy_id=id,status='Unlocked'):
#         return render(self.request, 'user/search.html',{'message':"Already Unlocked "})
#     else:
#         therapist = TherapistRegistration.objects.get(id=id)
#         fee = therapist.fees
#             context['fee'] = fee
#         return context

#     def post(self, request, *args, **kwargs):
#         id=self.request.GET['id']
#         user = Registration.objects.get(user_id=request.user.id)

#         if BookedTherapists.objects.filter(therapy_id=id,status='Unlocked'):
#             return render(request, 'user/search.html',{'message':"Already Unlocked "})
#         else:
#             therapy_id = request.GET['id']
#             therapist = TherapistRegistration.objects.get(id=therapy_id)
#             fee = therapist.fees


#             us=Registration.objects.get(user_id=request.user.id)
#             abc=BookedTherapists()
#             abc.payment_date = datetime.now().date()
#             expiry_date = abc.payment_date + timedelta(days=15)
#             abc.expiry_date = expiry_date
#             abc.user_id=us.id
#             abc.therapy_id=id
#             abc.status='Unlocked'
#             abc.save()
#             return redirect('user:index')


# class chpayment(LoginRequiredMixin,TemplateView):
#     template_name='user/payment.html'



        # return render(request, 'user/index.html',{'message':"Enquiry Sent"})


from datetime import date


class Mysolutions(LoginRequiredMixin, TemplateView):
    template_name = 'user/mysolutions.html'

    def get_context_data(self, **kwargs):
        context = super(Mysolutions, self).get_context_data(**kwargs)
        abc = Registration.objects.get(user_id=self.request.user.id)
        abc = Problems.objects.filter(user_id=abc.id)
        context = {
            'solutions': abc
        }
        return context


class thankyou(LoginRequiredMixin, TemplateView):
    template_name = 'user/thanks.html'



class booked_therapy(LoginRequiredMixin, TemplateView):
    template_name = 'user/bookedtherapist.html'

    def get_context_data(self, **kwargs):
        context = super(booked_therapy, self).get_context_data(**kwargs)
        abc = Registration.objects.get(user_id=self.request.user.id)
        pro = BookedTherapists.objects.filter(user_id=abc.id, status='Unlocked')
        today = date.today().isoformat()
        for i in pro:
            if i.expiry_date <= today:
                BookedTherapists.objects.get(id=i.id).delete()
            continue
        context = {
            'depre': pro
        }
        return context
# class Payment(LoginRequiredMixin,TemplateView):
#     template_name="user/payment.html"
#     def get_context_data(self, **kwargs):
#         id=self.request.GET['id']
#         cart = Problems.objects.get(id=id)
#         therapy=cart.therapy_id
#         abc = TherapistRegistration.objects.get(id=therapy)
#         fees=abc.fees
#         context={
#             "fee":fees
#         }
#         return context
#     def post(self,request,*args,**kwargs):
#         id=self.request.GET['id']
#         cart = Problems.objects.get(id=id)
#         cart.payment='Paid'
#         # cart.save()
#         # return render(request,'User/thanks.html',{'message':" payment Success"})
#         cart.payment_date = datetime.now().date()
#         # cart.payment_status = 'Paid'
#         cart.save()
#         expiry_date = cart.payment_date + timedelta(days=15)

#         difference=expiry_date-cart.payment_date
#         print(difference.days)
#         if difference.days >= 15:
#             return render(request, 'user/payment.html', {'message': "Pay Amount"})
#         else:
#         # Redirect or render appropriate page for expired payment
#             return render(request, 'User/thanks.html')


# class chpayment(TemplateView):
# def dispatch(self,request,*args,**kwargs):
#     id=self.request.GET['id']
#     cart = Problems.objects.get(id=id)
#     cart.payment='Paid'
#     cart.save()
#     return render(request,'User/thanks.html',{'message':" payment Success"})

# def view_solutions(request):
#     solutions = Problems.objects.all()  # Assuming you have a Solution model
#     for solution in solutions:
#         # Check if there is a corresponding therapist reply for each solution
#         therapist_reply_exists = Problems.objects.filter(answer=solution.answer).exists()
#         if therapist_reply_exists:
#             solution.has_reply = True
#         else:
#             solution.has_reply = False

#     return render(request, 'index.html', {'solutions': solutions})
