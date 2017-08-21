from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from forms import addadresForm, addVidsForm
from models import Adres, Person, Interest
from django.contrib.auth.models import User

# Create your views here.

def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = "No user find"
			return render_to_response('login.html', args)

	else:
		return render_to_response('login.html', args)

def logout(request):
	auth.logout(request)
	return redirect("/")
 
def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/auth/addadres/')
		else:
			args['form'] = newuser_form
	return render_to_response('register.html', args)

def test(request):
	return render_to_response('test.html', {'username': auth.get_user(request).username})

def addadres(request):
	adadr_form = addadresForm
	args = {}
	args.update(csrf(request))
	args['form'] = adadr_form
	if request.POST:
		newadres_form = adadr_form(request.POST)
		if newadres_form.is_valid():
			newadres_form.save()
			uname = request.user.username
			u = User.objects.get(username = uname)
			cb = u.id
			a = Adres.objects.get(adr = newadres_form.cleaned_data['adr'])
			p = Person(id = cb, created_by_id = cb)
			p.save()
			p.adres.add(a)
			p.save()
			return redirect('/auth/addvids')
		else:
			args['form'] = newadres_form
	return render_to_response('adadr.html', args)

def addVids(request):
	advids_form = addVidsForm
	args = {}
	args.update(csrf(request))
	args['form'] = advids_form
	if request.POST:
		newvids_form = advids_form(request.POST)
		if newvids_form.is_valid():
			uname = request.user.username
			u = User.objects.get(username = uname)
			cb = u.id
			p = Person.objects.get(created_by_id = cb)
			for x in newvids_form.cleaned_data['interests']:
				p.interest.add(x)
			p.save()
			return redirect('/auth/')
		else:
			args['form'] = newvids_form
	return render_to_response('advid.html', args)