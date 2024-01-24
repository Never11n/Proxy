from django.shortcuts import render
from django.views import View
from .forms import UserSiteForm


class CreateSiteView(View):
    def get(self, request):
        site_form = UserSiteForm()
        return render(request, 'main.html', {'form': site_form})

    def post(self, request):
        site_form = UserSiteForm(request.POST)
        if site_form.is_valid():
            user_site = site_form.save(commit=False)
            user_site.user = request.user
            user_site.save()
        return render(request, 'main.html', {'form': site_form})
