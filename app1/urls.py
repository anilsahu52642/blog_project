from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.views.generic import CreateView
from .models import blog
from .forms import *
from django.contrib.auth.urls import views as djangoviews

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home/',views.home,name='home_page'),
    path('signin/',views.signin,name='signin_page'),

    path('signup/',views.signup,name='signup_page'),
    
    path('profile/',views.profile,name='profile_page'),
    path('logout/',views.mylogout,name='logout_page'),

    path('pchange/',views.pchange,name='password_change_page'),
    path('createblog/',views.createblog,name='create_blog_page'),


    path('preset/',djangoviews.PasswordResetView.as_view(template_name='passwordreset.html',form_class=presetform,success_url='/preset/done/',email_template_name='email.html'),name='password_reset_page'),
    path('preset/done/', djangoviews.PasswordResetDoneView.as_view(template_name='presetdone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', djangoviews.PasswordResetConfirmView.as_view(template_name='presetconfirm.html',form_class=newpasswordform,success_url='/reset/done/'), name='password_reset_confirm'),
    path('reset/done/', djangoviews.PasswordResetCompleteView.as_view(template_name='presetsuccess.html'), name='password_reset_complete'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)