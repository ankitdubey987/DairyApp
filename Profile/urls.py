from django.urls import path
from Profile import views
app_name = 'profile'

urlpatterns = [
    path('',views.ProfileView.as_view(),name='home'),
    path('login/',views.ProfileLoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('signup/',views.ProfileRegisterView.as_view(),name='signup'),
]
