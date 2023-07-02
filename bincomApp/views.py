from django.shortcuts import render
from .models import AnnouncedPuResults
from .forms import NewPollingUnit, LocalGovtNames
# Create your views here.


#get staff ip address to avoid errors when creating new poll unit
def getUserIP(request):
   user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
   if user_ip_address:
        ip = user_ip_address.split(',')[0]
   else:
    ip = request.META.get('REMOTE_ADDR')
   return ip

#Create new poll unit
def New_PollUnit(request):
    if request.method == "POST":
     ip = getUserIP(request)
     form = NewPollingUnit(request.POST)
    
     if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user_ip_address = ip
            form_save.save()
            form = NewPollingUnit()
    else:
            form = NewPollingUnit()
    return render(request, 'newpollunit.html', {'form': form})


#fetch each polling unit total score 
def PollUnitResult(request):  
    results = AnnouncedPuResults.objects.raw('select result_id, sum(party_score) as totalscore from announced_pu_results group by polling_unit_uniqueid;')
    return render(request,"pollunitresult.html",{'results':results}) 


def ResultByLg(request):  
    


    # if request.method == "GET":
    form = LocalGovtNames()


    # if request.GET.get('type') == "submit":
    #         # test = form.cleaned_data
    test = request.GET.get('local_govt_name', '')

    execute = 'select result_id, lga.lga_id, lga_name, sum(party_score) as score from polling_unit, announced_pu_results, lga where lga.lga_id = polling_unit.lga_id and lga_name = %s group by lga.lga_id order by lga.lga_id;'
                
    results = AnnouncedPuResults.objects.select_related().raw(execute , [test])
    print(test)
    return render(request,"displaylgscore.html",{'results':results, 'form':form}) 
    # return render(request,"displaylgscore.html", {'form':form}) 


