from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import Profile
from frontend.forms import ProfileForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

def index(request):
	# request.session.set_test_cookie()


	profile_list = Profile.objects.all()
	profiles = {'profiles' : profile_list}

	visits = int(request.COOKIES.get('visits', '1'))
	reset_last_visit_time = False
	reset_last_visit_time_server = False
	response = render(request, 'index.html', profiles)

	context_dict = {'profiles': profile_list}


	visits_server = request.session.get('visits')

	if not visits_server:
		visits_server = 1

	reset_last_visit_time_server = False

	last_visit_server = request.session.get('last_visit_server')

	if last_visit_server:
		last_visit_time_server = datetime.strptime(last_visit_server[:-7], "%Y-%m-%d %H:%M:%S")

		if (datetime.now() - last_visit_time_server).seconds > 0:
			visits_server = visits_server + 1
			reset_last_visit_time_server = True
	else:
		reset_last_visit_time_server = True

	if reset_last_visit_time_server:
		request.session['last_visit_server'] = str(datetime.now())
		request.session['visits_server'] = visits_server

	context_dict['visits_server'] = visits_server




	if 'last_visit' in request.COOKIES:
		last_visit = request.COOKIES['last_visit']
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

		if (datetime.now() - last_visit_time).seconds > 5:
			visits = visits + 1
			reset_last_visit_time = True
	else:
		reset_last_visit_time = True
		context_dict['visits'] = visits

		response = render(request, 'index.html', context_dict)

	if reset_last_visit_time:
		response.set_cookie('last_visit', datetime.now())
		response.set_cookie('visits', visits)

	return response


# @login_required
def about(request):
	return render(request, 'about.html')


def add_profile(request):

	if request.method == 'POST':
		form = ProfileForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors

	else:
		form = ProfileForm()

	return render(request, 'add_profile.html', {'form' : form})



@login_required
def add_address(request):

	if request.method == 'POST':
		form = AddressForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	else:
		form = AddressForm()

	return render(request, 'add_address.html', {'form' : form})




def register(request):

	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED!"
    	request.session.delete_test_cookie()



	registerd = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit = False)
			profile.user = user


			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registerd = True

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'register.html', {'user_form' : user_form, 'profile_form' : profile_form, 'registerd' : registerd})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')


		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/frontend/')
			else:
				return HttpResponse('Your Account is not active')
		else:
			print "Invalid login info, {0}, {1}" . format(username, password)
			return HttpResponse("Invlaid login details")
	else:
		return render(request, 'login.html')


@login_required
def restricted(request):
	return HttpResponse("You are not logged in")



@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/frontend/')


