from django.shortcuts import render
def mileage(request):
    distance=int(request.POST.get('distance','0'))
    fuel=int(request.POST.get('fuel','0'))
    mileage=distance/fuel if request.method=='POST'else 0
    print("fuel=",fuel)
    print("distance=",distance)
    print("mileage=",mileage)
    return render(request,'mathapp/math.html',{'distance':distance,'fuel':fuel,'mileage':mileage})