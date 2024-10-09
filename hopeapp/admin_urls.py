from django.urls import path
from hopeapp.admin_views import index,category,view_therapist,view_users,RemoveUser,RemoveTherapist,Therapist_Verify,ApproveView,ViewCategory,RemoveCategory,View_Feedback,ViewBookedTherapist,therapist_users_booking,ViewMore,userbookedtherapist
urlpatterns = [
    path('', index.as_view()),

    path('category',category.as_view(),name='category'),
    path('view_category',ViewCategory.as_view(),name='category'),
    path('view_therapist',view_therapist.as_view()),
    path('view_users',view_users.as_view()),
    path('RemoveUser',RemoveUser.as_view()),
    path('RemoveCategory',RemoveCategory.as_view()),

    path('RemoveTherapist',RemoveTherapist.as_view()),
    path('Therapist_Verify',Therapist_Verify.as_view()),
    path('ApproveView',ApproveView.as_view()),
    path('view_feedback',View_Feedback.as_view()),
    path('ViewBookedTherapist',ViewBookedTherapist.as_view()),
    path('therapist_users_booking',therapist_users_booking.as_view(),name='therapist_users_booking'),
    path('viewmore',ViewMore.as_view()),
    path('userbookedtherapist',userbookedtherapist.as_view())

]
def urls():
    return urlpatterns, 'admin','admin'