from django.http import JsonResponse
from django.views import View
from models import User


# Create your views here.
class UserView(View):

    def get(self, request):
        users = User.objects.all()
        if len(users) > 0:
            datos = {'message': "Success", 'users': users}
        else:
            datos = {'message': "Users no found ..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
