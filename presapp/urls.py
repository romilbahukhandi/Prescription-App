from django.conf.urls import url
from presapp import views
from .views import indexpage
from .views import new_patient
from .views import get_template
#from .views import HelloPDFView

urlpatterns = [
    url(r'^$', views.indexpage, name='index'),
    url(r'^new/$', views.new_patient, name='newpatient'),
    url(r'^view/(?P<pk>\d+)/$', views.viewpatient, name='viewpatient'),
    url(r'^addprescription/(?P<pid>\d+)/$', views.newtemplate, name='newtemplate'),
    url(r'^templates/(?P<patid>\d+)/$', views.viewprescription, name='templates'),
    #url(r'^printtemplate/(?P<tempid>\d+)$', views.pdfexport, name='pdfexport'),
    url(r'^viewprescription/(?P<tid>\d+)/$', views.get_template, name='viewtemplates'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^logout/$', views.logoutview, name='logout'),
    #url(r"^pdf.pdf$", HelloPDFView.as_view(), name='pdf')
    ]


'''
url(r'^/new/$', views.newpatient, name='new')
'''
