
from django import forms
from .models import PollingUnit

class NewPollingUnit(forms.ModelForm):
  class Meta:
    model = PollingUnit
    fields = ["polling_unit_id", "ward_id", "lga_id", "uniquewardid", "polling_unit_number", "polling_unit_name", "polling_unit_description", "lat", "long", "entered_by_user", "user_ip_address"]
    labels = {'polling_unit_id': "Unit Id", 'ward_id' : "Ward Id", 'lga_id' : "LGA Id", 'uniquewardid' : "UnqWard Id", 'polling_unit_number' : "Unit Number", 'polling_unit_name' : "Unit Name", 'polling_unit_description' : "Unit Description", 'lat' : "LAT", 'long' : "LONG", 'entered_by_user' : "Staff Name"}
    
