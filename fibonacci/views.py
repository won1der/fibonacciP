from django.http import HttpResponse
import time

def calculateFibnacci(n):
    first=1
    second=1
    num = 0

    if(n==1):
      return 1
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
            start_t=time.time()
            nth = request.POST.get('nth', 'null')
            if (nth == 'null'):
                return HttpResponse('Value of n is incorrect')
            try:
                n=int(nth)
                answer = calculateFibnacci(n)
                end_t=time.time()-start_t
                s=""+nth+"th Fibonacci number is "+str(answer)+".\n Time required in computation is "+str(end_t)+" sec"
                return HttpResponse(s)
            except ValueError:
                s="Please enter a number as argument"
                return HttpResponse(s)

    else:
        return HttpResponse('Network Problem')


