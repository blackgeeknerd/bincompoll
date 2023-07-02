
from django import forms
from .models import PollingUnit

class NewPollingUnit(forms.ModelForm):
  class Meta:
    model = PollingUnit
    fields = ["polling_unit_id", "ward_id", "lga_id", "uniquewardid", "polling_unit_number", "polling_unit_name", "polling_unit_description", "lat", "long", "entered_by_user", "user_ip_address"]
    labels = {'polling_unit_id': "Unit Id", 'ward_id' : "Ward Id", 'lga_id' : "LGA Id", 'uniquewardid' : "UnqWard Id", 'polling_unit_number' : "Unit Number", 'polling_unit_name' : "Unit Name", 'polling_unit_description' : "Unit Description", 'lat' : "LAT", 'long' : "LONG", 'entered_by_user' : "Staff Name"}
    

class LocalGovtNames(forms.Form):
  CHOICES = (
     ('Aniocha North', 'Aniocha North'),
    ('Aniocha - South', 'Aniocha - South'),
    ('Ethiope East', 'Ethiope East'),
    ('Ethiope West', 'Ethiope West'),
    ('Ika North - East', 'Ika North - East'),
    ('Ika - South', 'Ika - South'),
    ('Isoko North', 'Isoko North'),
    ('Ndokwa East','Ndokwa East'),
    ('Ndokwa West', 'Ndokwa West'),
    ('Okpe', 'Okpe'),
    ('Oshimili - North', 'Oshimili - North'),
    ('Isoko South', 'Isoko South'),
    ('Oshimili - South', 'Oshimili - South'),
    ('Patani', 'Patani'),
    ('Sapele', 'Sapele'),
    ('Udu', 'Udu'),
    ('Ughelli North', 'Ughelli North'),
    ('Ughelli South',  'Ughelli South'),
    ('Ukwuani', 'Ukwuani'),
    ('Uvwie', 'Uvwie'),
    ('Bomadi', 'Bomadi'),
    ('Burutu', 'Burutu'),
    ('Warri North', 'Warri North'),
    ('Warri South', 'Warri South'),
    ('Warri South West', 'Warri South West'),
  )
  
  local_govt_name = forms.ChoiceField(choices=CHOICES)










