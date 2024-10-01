from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse(f"response to this request {request}")

    def post(self, request):
        pass
