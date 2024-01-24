from django.shortcuts import render, redirect
from django.views import View
from .forms import UserSiteForm
from .models import UserSite


class CreateSiteView(View):
    def get(self, request):
        site_form = UserSiteForm()
        user_sites_list = UserSite.objects.filter(user=request.user)
        return render(request, 'main.html', {'form': site_form, 'sites': user_sites_list})

    def post(self, request):
        site_form = UserSiteForm(request.POST)
        if site_form.is_valid():
            user_site = site_form.save(commit=False)
            user_site.user = request.user
            user_site.save()
            return redirect('main')
        return render(request, 'main.html', {'form': site_form, 'success_message': 'Site created successfully'})


def proxy(request, site_name):
    return render(request, 'proxy_site.html', {'site_name': site_name})
