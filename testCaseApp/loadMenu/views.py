from django.shortcuts import render
from django.views.generic import View
from menuApp.models import MenuItem

class IndexView(View):
    def get(self, request, **kwargs):
        menu_item = MenuItem.objects.get(name=kwargs['name'])
        return render(request, 'index.html')

class IndexDetail(View):
    def get(self, request, params=None):
        return render(request, 'index.html')