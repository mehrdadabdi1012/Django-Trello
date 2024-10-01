from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse


class AccountView(View):
    def get(self, request):
        return HttpResponse("this is accounts page")

    def post(self, request):
        pass
