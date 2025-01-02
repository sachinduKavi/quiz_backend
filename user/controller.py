from django.http import HttpResponse



class Controller:
    
    # New user registration
    def userRegistration(request):
        print('user registration...')
        
        return HttpResponse("Hello WOrld")