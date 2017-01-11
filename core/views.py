from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from core.models import Service
from core import forms


def main(request):
    services = Service.objects.all()

    return render(request, 'main.html', {
        'services': services,
    })


class ServiceView(View):
    def get(self, request, id):
        try:
            service = Service.objects.get(id=int(id))
        except:
            raise Http404

        return render(request, 'service.html', {
            'service': service,
        })


def login(request):
    redirect = request.GET.get('continue', '/success')
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(redirect)
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {
        'form': form,
    })


def signup(request):
    redirect = request.GET.get('continue', '/success')
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(redirect)
    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {
        'form': form,
    })


@login_required(redirect_field_name='continue')
def login_success(request):
    redirect = request.GET.get('continue', '/')
    return HttpResponseRedirect(redirect)


def logout(request):
    redirect = request.GET.get('continue', '/')
    auth.logout(request)
    return HttpResponseRedirect(redirect)
