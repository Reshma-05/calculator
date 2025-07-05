from django.shortcuts import render

def.home(request):
    result = None
    if request.method == 'POST':
        a = int(request.POST.get('Num1'))
        b = int(request.POST.get('Num2'))
        op = request.POST.get('Op')
        if op=='+':
            result = a+b
        elif op =='-':
            result = a-b
        elif op == '*':
            result =a*b
        elif op == '/':
            result= a/b
        else:
            return render(request,'home.html',{'error':'error'})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})            


