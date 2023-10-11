from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


class register(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})

class login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # Set the session expiry to 0 seconds to close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set the session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # The browser session will be as long as the session cookie time defined in settings.py.
        return super(login, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # Redirect to the home page if a user tries to access the login page while logged in.
        if request.user.is_authenticated:
            return redirect(to='home')

        # Process the dispatch as it otherwise normally would.
        return super(login, self).dispatch(request, *args, **kwargs)

