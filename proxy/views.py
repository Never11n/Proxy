from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

