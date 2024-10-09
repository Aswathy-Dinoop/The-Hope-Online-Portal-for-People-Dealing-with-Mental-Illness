from django.urls import path
from hopeapp import therapist_views

from hopeapp.therapist_views import index,Profile,Post_Depressions,ViewDepressions,RemoveDep,UpdateDep,ViewProblems,UpdateProfile
urlpatterns = [
    path('', index.as_view()),
    path('postdepressions',Post_Depressions.as_view()),
    path('ViewDepressions',ViewDepressions.as_view()),
    path('myprofile',Profile.as_view()),
    path('remove',RemoveDep.as_view()),
    path('update',UpdateDep.as_view()),
    path('ViewProblems',ViewProblems.as_view()),
    path('updateprofile',UpdateProfile.as_view()),
    path('view_problem',therapist_views.view_problem,name='view_problem'),

]
def urls():
    return urlpatterns, 'therapist','therapist'