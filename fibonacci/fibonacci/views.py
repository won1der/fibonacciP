from django.http import HttpResponse

def calculateFibnacci(n):
    first=0
    second=1
    num = 0

    if(n==1):
      return 0
    if(n==2):
       return 1
    else:
        for i in range(n-2):
            num=first+second
            first=second
            second=num

    return num

def fibonacci(request):
    if request.method == "POST":
        nth = request.POST.get('nth', 'null')
        if (nth == 'null'):
            return HttpResponse('Value of n is incorrect')
        answer = calculateFibnacci(int(nth))
        return HttpResponse(answer)

    else:
        return HttpResponse('Network Problem')



