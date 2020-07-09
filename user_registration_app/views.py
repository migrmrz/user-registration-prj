from django.shortcuts import render
from user_registration_app.models import User
from user_registration_app.forms import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'user_registration_app/index.html')

def user_info(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users': user_list}
    return render(request, 'user_registration_app/userInfo.html', user_dict)

def user_signup(request):
    user_registration_form = UserRegistrationForm()
    print(user_registration_form, type(user_registration_form))
    if request.method == "POST":
        user_registration_form = UserRegistrationForm(request.POST)
        if user_registration_form.is_valid():
            user_registration_form.save(commit=True)
            return index(request)
        else:
            print("Error. Invalid form")
    return render(request, 'user_registration_app/userSignup.html', {'user_registration_form': user_registration_form})
