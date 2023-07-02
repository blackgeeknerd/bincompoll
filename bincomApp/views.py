from django.shortcuts import render
from .models import AnnouncedPuResults
from .forms import NewPollingUnit
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

    ip = getUserIP(request)
    
    if request.method == "POST":
    
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