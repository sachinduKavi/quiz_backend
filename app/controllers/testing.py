from django.http import JsonResponse

def testing(request):
    print(request)
    return  JsonResponse({
        "name": "sachindu",
        "age": 25
    })