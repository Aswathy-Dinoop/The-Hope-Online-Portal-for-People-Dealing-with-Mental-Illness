from django.urls import path
from hopeapp import user_views
from hopeapp.user_views import index,Profile,ViewAllDepressions,SingleDepressions,Search,SingleTherapists,Mysolutions,thankyou,UpdateProfile,booked_therapy,feedback
urlpatterns = [
    path('', index.as_view(),name='index'),
    path('ViewAllDepressions',ViewAllDepressions.as_view(),name='ViewAllDepressions'),
    path('singlepageview',SingleDepressions.as_view(),name="singlepageview"),
    path('myprofile',Profile.as_view(),name='myprofile'),
    path('search',Search.as_view(),name='search'),
    path('singletherapist',SingleTherapists.as_view(),name='singletherapist'),
    path('enquiries',Mysolutions.as_view(),name='enquiries'),
    # path('payment',userviews.payment,name='payment'),
    # path('chpayment',chpayment.as_view(),name='chpayment'),

    path('updateprofile',UpdateProfile.as_view(),name='updateprofile'),
    path('thankyou',thankyou.as_view(),name='thankyou'),
    path('booked_therapy',booked_therapy.as_view(),name="booked_therapy"),

    path('feedback',feedback.as_view()),


]
def urls():
    return urlpatterns, 'user','user'