import json
from django.http import JsonResponse
from django.views import View
from api.models import User, Categoria
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            users = list(User.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
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

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            users = User.objects.get(id=id)
            users.nombre_user = jd['nombre_user']
            users.apellido_user = jd['apellido_user']
            users.correo_user = jd['correo_user']
            users.contraseña_user = jd['contraseña_user']
            users.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Users no found ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Users no found ..."}
        return JsonResponse(datos)

#vista de la categoria
class CategoriaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            categories = list(Categoria.objects.filter(id=id).values())
            if len(categories) > 0:
                category = categories[0]
                datos = {'message': "Success", 'categories': category}
            else:
                datos = {'message': "Companies no found ..."}
            return JsonResponse(datos)
        else:
            categories = list(Categoria.objects.values())
            if len(categories) > 0:
                datos = {'message': "Success", 'categorias': categories}
            else:
                datos = {'message': "Categoria no found ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Categoria.objects.create(nombre_categoria=jd['nombre_categoria'], tipo_categoria=jd['tipo_categoria'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id: int = 0):
        jd = json.loads(request.body)
        categories = list(Categoria.objects.filter(id=id).values())
        if len(categories) > 0:
            categories = Categoria.objects.get(id=id)
            categories.nombre_categoria = jd['nombre_categoria']
            categories.tipo_categoria = jd['tipo_categoria']
            categories.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Categoria no found ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        categories = list(Categoria.objects.filter(id=id).values())
        if len(categories) > 0:
            Categoria.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Categoria no found ..."}
        return JsonResponse(datos)

