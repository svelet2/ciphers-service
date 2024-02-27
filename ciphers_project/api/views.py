from django.http import JsonResponse

def greetings(request):
    result = {"message": "Welcome to the Ciphers service!"}
    return JsonResponse(result)

