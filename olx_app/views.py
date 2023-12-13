from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from .models import *


# Create your views here.

class product_upload(generic.CreateView):
    form_class = product_form
    template_name = 'upload.html'
    success_url = reverse_lazy('view')


class product_view(generic.ListView):
    model = product_model
    template_name = 'list.html'
    context_object_name = 'files'

    def get(self, request):
        a = self.model.objects.all()
        return render(request, self.template_name, {'files': a})


class product_delete(generic.DeleteView):
    model = product_model
    template_name = 'delete.html'
    success_url = reverse_lazy('view')


class product_update(generic.UpdateView):
    model = product_model
    template_name = 'update.html'
    fields = ['name', 'price', 'colour']
    success_url = reverse_lazy('view')
