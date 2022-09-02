import json
from django.http import JsonResponse
from django.views import View
from api.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):
        if(id>0):
            users= list(User.objects.filter(id=id).values())
            if len(users) > 0:
                user=users[0]
                datos = {'message': "Success", 'users': user}
            else:
                datos = {'message': "User no found ..."}
            return JsonResponse(datos)
        else:
            users = list(User.objects.values())
            if len(users) > 0:
                datos = {'message': "Success", 'users': users}
            else:
                datos = {'message': "Users no found ..."}
            return JsonResponse(datos)


    def post(self, request):
        jd = json.loads(request.body)
        User.objects.create(nombre_user=jd['nombre_user'], apellido_user=jd['nombre_user'],
                            correo_user=jd['correo_user'], contraseña_user=jd['contraseña_user'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass
