# students/middleware.py

from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectToHomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the requested URL is the root URL, redirect to the home page
        if request.path == '/':
            return HttpResponseRedirect(reverse('home'))

        response = self.get_response(request)
        return response
