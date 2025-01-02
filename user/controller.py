from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.http import require_POST
from .models import user_collection, User
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class Controller:
    
    
    # New user registration
    @require_POST
    @csrf_exempt
    @staticmethod
    def userRegistration(request):
        proceed = False 
        content = None
        message = None
        body = json.loads(request.body)
        
        
        user_details = {
            "name": body.get('name'),
            "email": body.get('email'),
            "password": body.get('password')
        }
        
        try:
            db_response = user_collection.insert_one(user_details)
            if db_response.acknowledged:
                proceed = True
        except Exception as e:
            print(e)
            message = e
        
        
        
        # Response to the client
        return JsonResponse({
            "proceed": proceed,
            "content": content,
            "message": message
        })
        
        
        
    # Check user credentials 
    @require_POST
    @csrf_exempt
    @staticmethod
    def authentication(request): 
        proceed = False 
        content = None
        message = None
        body = json.loads(request.body)
        
        
        db_response = user_collection.find_one({"email": body.get('email')})
        if db_response:
            user = User(db_response)
            print(user)
        
        # Response to the client
        return JsonResponse({
            "proceed": proceed,
            "content": content,
            "message": message
        })