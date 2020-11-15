from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json
from django.contrib.auth.models import User
# Create your views here.
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def api_login(request):
    data=json.loads(request.body)
    """
    CSRF exempt login for REST API clients

    :param request:
    :return:
    """
    # Take username/password form variables,
    # validate them
    # create session
    status=authenticate(username=data["username"],password=data["password"])
    print(status)
    user=User.objects.get(username=data["username"])
    print(user)#shivansh.1923cs1076
    if  user is not None:
        response=login(request,user)#nul;
        print(user.is_authenticated)#True
        print(request.session)#<django.contrib.sessions.backends.db.SessionStore object at 0x7f0c082f5e80>
                # print(request.META['HTTP_COOKIE'])#sessionid=ky8pp6z1p0m6znxtxq5efpllpe6wsnb0   (after successful login only this cookie is generated and for the same ssession that is until logout the sessionid remains the same )
        permission_classes=[permissions.IsAuthenticated]
        print(permission_classes)
        return JsonResponse(response,safe=False)
    else:
        return JsonResponse("nope",safe=False)  


# @csrf_exempt
def api_logout(request):
    """
    CSRF exempt login for REST API clients

    :param request:
    :return:
    """
    logout(request)
    return HttpResponse('Success')
