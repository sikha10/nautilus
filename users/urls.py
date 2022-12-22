from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views
from .forms import UserSignInView

urlpatterns = [
    path('signup/', signup, name='user-signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='sign_in.html', authentication_form=UserSignInView), name='user-signin',),

]