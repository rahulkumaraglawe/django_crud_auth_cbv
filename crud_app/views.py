from django.shortcuts import render
from .models import Hotel
from django import views
from .forms import HotelForm

# Create your views here.


class SaveView(views.View):
    
    template_name = 'crud_app/save.html'
    form = HotelForm
    
    def get(self, request):
        return render(request, self.template_name, context={'form':self.form})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            form = self.form()
            return render(request, self.template_name, context = {'form':form})
        return render(request, self.template_name, context = {'form':form})
        
        
class ShowView(views.View):
    template_name = 'crud_app/show.html'
    
    def get(self, request):
        h = Hotel.objects.all()
        return render(request, self.template_name, context = {'object':h})