from django.shortcuts import render

# Create your views here.
def my_fillter(request):
    # return render(request,'myfillter.html',{'value':100})

    # return render(request,'myfillter.html',{'value':"rahul"})

    # return render(request,'myfillter.html',{'value':"i am Developer"})

    # data=""
    # return render(request,'myfillter.html',{'value':data})

    # data=None
    # return render(request,'myfillter.html',{'value':data})

    # data=[
    #     {'name':'Rahul','age':24},
    #     {'name':'Soarabh','age':28},
    #     {'name':"Arun",'age':24}
    # ]
    # return render(request,'myfillter.html',{'value':data})
    
    return render(request,'myfillter.html',{'value':["Rahul","Age:24","City:Bhopla"]})    
