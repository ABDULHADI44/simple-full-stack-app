from django.contrib import admin
from django.urls import path
from accounts import views
#from accounts.views import login_view, dashboard_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='home'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('signout', views.signout, name = 'signout'),
    ] 