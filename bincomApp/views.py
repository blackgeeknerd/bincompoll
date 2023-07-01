from django.shortcuts import render
from .models import AnnouncedPuResults
from .forms import NewPollingUnit
# Create your views here.

def New_PollUnit(request):
  if request.method == "POST":
    form = NewPollingUnit(request.POST)
    if form.is_valid():
      form.save()
      form = NewPollingUnit()
    #   return redirect("pollunitresults")
  else:
      form = NewPollingUnit()
  return render(request, 'newpollunit.html', {'form': form})



def PollUnitResult(request):  
    results = AnnouncedPuResults.objects.raw('select result_id, sum(party_score) as totalscore from announced_pu_results group by polling_unit_uniqueid;')
    print(results)
    
    return render(request,"pollunitresult.html",{'results':results}) 