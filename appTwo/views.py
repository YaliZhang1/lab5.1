from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from
from appTwo.forms import UserProfileInfoForm, UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'appTwo/index.html')

@login_required
def special(request):
    return HttpResponse("You're logged in,cool!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def relative(request):
    return render(request,'appTwo/relative_url_templates.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
                profile.save()

                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'appTwo/registration.html',
                {'user_form': user_form,
                 'profile_form' : profile_form,
                 'registered': registered })
    
    def user_login(request):
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate

            if user:
                if uesr.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse
            else:
                print('Someone trid to login')
                print(username,password)
                return HttpResponse('invalid login!')
        else:
            render(request,'appTwo/login.html',{}) 
    #user_list = User.objects.order_by('first_name')
    #user_dict = {"user":user_list}
    #return render(request,'apptwo/user.html',context=user_dict)