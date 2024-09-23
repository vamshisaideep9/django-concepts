from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.



def homepage_view(request):
    context = {
        'message' : 'Welcome to the homepage!',
        'user' : 'vamshisaideep',
    }
    return render(request, 'revision/new_url.html', context)


# class ContactView(View):
#     template_name = 'revision/contact.html'

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)
    
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         message = request.POST.get('message')

#         if name and message:
#             return HttpResponse(f"Thank you {name}, your message has been received.")
#         else:
#             return HttpResponse("Please fill out both fields.")


class ContactView(View):
    template_name = 'revision/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args,**kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'form':form})