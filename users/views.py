from django.shortcuts import render
from django.views import View
from  users.models import TovarModel
def index(request):
    return render (request, 'index.html')

class TovarView(View):
    def get(self, request):
        a = TovarModel.objects.all()
        return render(request, 'order.html', {'a':a})