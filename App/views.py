from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.


def index(request):
    pp = ProminentParameter.objects.all()
    ac = AtmosCondition.objects.all()
    pc = PondCondition.objects.all()
    if(request.method == "POST"):
        parameters = dict()
        for i in request.POST:
            if("para" in i):
                if(len(request.POST.get(i)) > 0):
                    parameters[i[5:]] = float(request.POST.get(i))
        result = list()
        for i in parameters:
            para = ProminentParameter.objects.get(id=i)
            if(para.lower_boundary > parameters[i] or para.upper_boundary < parameters[i]):
                atmos = AtmosCondition.objects.get(
                    id=float(request.POST.get("atmos")))
                pond = PondCondition.objects.get(id=request.POST.get("pond"))
                combination = Combinations.objects.get(
                    ppname=para, acname=atmos, pcname=pond)
                result.append(combination.composition +
                              " is used to stabilize "+str(combination.ppname))
        if(len(result) > 0):
            messages.success(
                request, "To stabilize your pond use the following chemicals in the metioned compositions:")
            for i in range(len(result)):
                messages.success(request, str(i+1)+". "+result[i])
        return redirect("App:index")
    return render(request, "App/index.html", {"parameters": pp, "atmos": ac, "pond": pc})
