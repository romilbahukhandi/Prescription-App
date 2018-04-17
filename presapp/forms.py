from django import forms
from presapp.models import Patient, presciptiontemplates
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets
from ckeditor.widgets import CKEditorWidget
from gulabjamun import settings
from django.core.exceptions import ValidationError
from material import Layout, Row, Fieldset, Span5

#from django.contrib.flatpages.models import FlatPage

BIRTH_YEAR_CHOICES = ((1900),	(1901),	(1902),	(1903),	(1904),	(1905),	(1906),	(1907),	(1908),	(1909),	(1910),	(1911),	(1912),	(1913),	(1914),	(1915),	(1916),	(1917),	(1918),	(1919),	(1920),	(1921),	(1922),	(1923),	(1924),	(1925),	(1926),	(1927),	(1928),	(1929),	(1930),	(1931),	(1932),	(1933),	(1934),	(1935),	(1936),	(1937),	(1938),	(1939),	(1940),	(1941),	(1942),	(1943),	(1944),	(1945),	(1946),	(1947),	(1948),	(1949),	(1950),	(1951),	(1952),	(1953),	(1954),	(1955),	(1956),	(1957),	(1958),	(1959),	(1960),	(1961),	(1962),	(1963),	(1964),	(1965),	(1966),	(1967),	(1968),	(1969),	(1970),	(1971),	(1972),	(1973),	(1974),	(1975),	(1976),	(1977),	(1978),	(1979),	(1980),	(1981),	(1982),	(1983),	(1984),	(1985),	(1986),	(1987),	(1988),	(1989),	(1990),	(1991),	(1992),	(1993),	(1994),	(1995),	(1996),	(1997),	(1998),	(1999),	(2000),	(2001),	(2002),	(2003),	(2004),	(2005),	(2006),	(2007),	(2008),	(2009),	(2010),	(2011),	(2012),	(2013),	(2014),	(2015),	(2016),	(2017),	(2018))

GenderChoices = ((None, ''), ('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
age_dob = (('a', 'Age'), ('d', 'DOB'))

class newpatientform(forms.ModelForm):
    fname = forms.CharField(max_length=100, label="Name", required=True)
    agechoice = forms.ChoiceField(label="Age/DOB", choices=age_dob, widget=forms.RadioSelect)
    dob = forms.DateField(required=False, label="Date Of Birth",widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    payear = forms.IntegerField(required=False, label="Age", widget=forms.NumberInput)
    sex = forms.ChoiceField(choices=GenderChoices, label=" Gender")
    cellular = forms.IntegerField(required=True, label="Mobile Number", widget=forms.NumberInput)
    layout = Layout(Span5('fname'), 'agechoice', Row('dob', 'payear'), Row('sex', 'cellular'))

    class Meta:
        model = Patient
        fields = ['fname',  'payear', 'sex', 'cellular']

class templateform(forms.ModelForm):
    template = forms.CharField(widget=forms.Textarea, label='')
    draft = forms.BooleanField(required=False)
    layout = Layout(Fieldset('Template'), ('template'), ('draft'))
    class Meta:
        model = presciptiontemplates
        fields = ['template', 'draft']


class loginForm(forms.Form):
    uname = forms.CharField(label='User Name', max_length=100)
    pswrd = forms.CharField(label='Password',widget=forms.PasswordInput)
    layout = Layout(Span5('uname'), ('pswrd'))




"""
 New Pateint FOrm

 def __init__(self, *args, **kwargs):
     super(newpatientform, self).__init__(*args, **kwargs)
     for key in self.fields:
         self.fields[key].required = True

 class Meta:
     model = Patient
     fields = ['fname',  'payear', 'sex', 'cellular' ]
     #'dob',
     labels = {
         "fname": _("Name"),
         #'dob': _("Date Of Birth"),
         'sex': _("Gender"),
         'cellular': _("Phone Number"),
         'payear': _("Age"),
     }
     widgets = {
          #'dob': forms.DateInput(),
          'payear': forms.NumberInput(),
          'sex': forms.RadioSelect(choices=GenderChoices),
          'cellular': forms.NumberInput(),
          'fname': forms.TextInput(),
     }
     required = {
         "fname": True,
         "sex": True,
     }
     input_formats = settings.DATE_INPUT_FORMATS
     """
"""
             widgets = {
                 'template': CKEditorWidget(),
             }
             labels = {
                 "templateid": _("Patient ID"),
                 }
             """
