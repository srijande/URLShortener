from django.shortcuts import render
from django.http import HttpResponse
from .models import Shortener
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View

from .models import Shortener
from .forms import ShortenURLForm


def index(request):
    return render(request, 'home.html')


def redirector(request, shortened_link):
    data = Shortener.objects.get(shortened_link=shortened_link)
    print("===")
    print(data)
    return redirect(data.original_link)


class HomeView(View):

	def get(self, request, *args, **kwargs):
		form = ShortenURLForm()
		context = {
			'form': form
		}
		return render(request, 'home.html', context)

	def post(self, request, *args, **kwargs):
		form = ShortenURLForm(request.POST)
		context = {
			'form': form
		} 
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = Shortener.objects.get_or_create(original_link=new_url)
			context = {
				'obj': obj,
				'created': created
			}
		return render(request, 'home.html', context)





def create_post(request): 
	response_data = {}
	
	if request.POST.get('action') == 'post':

		new_url = request.POST.get('url')
		obj, created = Shortener.objects.get_or_create(original_link=new_url)
		context = {
			'obj': obj,
			'created': created
		}
		print(obj.shortened_link)
		response_data['shortened_link'] = obj.shortened_link
		return JsonResponse(response_data)
