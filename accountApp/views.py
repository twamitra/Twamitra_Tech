from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate , login
from accountApp.models import User
from django.contrib import messages
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from twamitraApp.forms import FormWithCaptcha

def dashboard(request):
  return render(request, 'home.html')

# Create your views here.
def registeruser(request):
    if request.method == "POST":
        email = request.POST.get("email",None)
        password1 = request.POST.get("password1",None)
        password2 = request.POST.get("password2",None)
        form = FormWithCaptcha(request.POST)
        if(form.is_valid()):
            print(email)
            print(password1)
            print(password2)
            if(password1 != password2):
                messages.success(request, "Password mismatch!")
                return render( request, "register.html", {"email":email})                
            try:
                user = User.objects.create_user(username=email, email=email,password=password1,is_customer=True)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            except:
                messages.success(request, " Username already Taken! Try With another Username...")
                return render( request, "register.html", {"email":email})
            return redirect ('home')
        else:
            messages.error(request, "reCAPTCHA validation failed.")
    else:
        form = FormWithCaptcha()

    return render(request, "register.html", {"form": form})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
        except:
              messages.add_message(request, messages.INFO, "User does not exist")
              print("User does not exist")
        user = authenticate(request, email = email, password = password)    
        
        if user is not None:
              message ={
                  'status':'success',
                  'message':'Logged in successfully'
              }
              messages.success(request, message)
              login(request, user)
              print("logged in")
              return redirect('userDashboard', 'service')
        else:
            messages.error(request,  "Invalid credentials")
          
    return render(request,'login.html')



def logoutuser(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render ( request, "dashboard.html")

