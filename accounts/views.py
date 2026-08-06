from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, ProfileUpdateForm, UserUpdateForm
from blog.models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        messages.success(self.request, _('Welcome! Your account has been created successfully.'))
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Register')
        return context


def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('Welcome back!'))
            next_url = request.GET.get('next', 'blog:home')
            return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {
        'form': form,
        'title': _('Login')
    })


def logout_view(request):
    logout(request)
    messages.info(request, _('You have been logged out.'))
    return redirect('blog:home')


@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Profile updated successfully!'))
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': _('My Profile')
    })
