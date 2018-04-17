from django.shortcuts import render, redirect, render_to_response, get_list_or_404, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from presapp.models import Patient, presciptiontemplates
from presapp.forms import newpatientform, templateform, loginForm
from django.contrib import messages
from io import BytesIO
from reportlab.pdfgen import canvas
from django.core import serializers
import json
from django.contrib.auth import authenticate, login, logout
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404
from datetime import datetime
from easy_pdf.views import PDFTemplateView
# Create your views here.


def indexpage(request):
    patlist = Patient.objects.all().order_by('-rdate')
    page = request.GET.get('page', 1)
    paginator = Paginator(patlist, 30)
    try:
        patlist = paginator.page(page)
    except PageNotAnInteger:
        patlist = paginator.page(1)
    except EmptyPage:
        patlist = paginator.page(paginator.num_pages)
    return render(request, 'presapp/index.html', {'patlist': patlist})


def new_patient(request):
    if request.method == "POST":
        form = newpatientform(request.POST)
        if form.is_valid():
            patient = Patient()
            patient.fname = form.cleaned_data.get('fname')
            agechoice = form.cleaned_data.get('agechoice')
            if agechoice == 'a':
                patient.payear = form.cleaned_data.get('payear')
            else:
                patient.dob = form.cleaned_data.get('dob')
            patient.sex = form.cleaned_data.get('sex')
            patient.cellular = form.cleaned_data.get('cellular')
            patient.save()
            messages.success(request, 'User Added successfully!')
            return redirect('index')
        else:
            messages.success(request, 'Please Recheck Your Form')
            # return render(request, 'presapp/new.html', {'form': form})
    else:
        form = newpatientform(request.POST)
        # messages.success(request, 'Request Invalid Please Try Again')
    return render(request, 'presapp/newpatient.html', {'form': form})


def viewpatient(request, pk):
    post = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = newpatientform(request.POST ,instance=post)
        if form.is_valid():
            patient = Patient()
            patient.patientid = pk
            patient.fname = form.cleaned_data.get('fname')
            agechoice = form.cleaned_data.get('agechoice')
            patient.sex = form.cleaned_data.get('sex')
            patient.cellular = form.cleaned_data.get('cellular')
            if agechoice == 'a':
                patient.payear = form.cleaned_data.get('payear')
            else:
                patient.dob = form.cleaned_data.get('dob')
            patient.save()
            messages.success(request, 'Updated Successfully')
        return redirect('index')
    else:
        form = newpatientform(instance=post)
    return render(request, 'presapp/view.html', {'form': form})


def newtemplate(request, pid):
    patientdetails = Patient.objects.get(patientid=pid)
    form = templateform(request.POST)
    if request.method == "POST":
        form = templateform(request.POST)
        if form.is_valid():
            form.save(commit=False)
            Presciptiontemplates = presciptiontemplates()
            Presciptiontemplates.patientid = pid
            Presciptiontemplates.savedate = datetime.now()
            Presciptiontemplates.template = form.cleaned_data.get('template')
            Presciptiontemplates.draft = form.cleaned_data.get('draft')
            Presciptiontemplates.save()
            messages.success(request, 'Prescription Saved Successfully')
        else:
            messages.error(request, 'Please Try Again')
        return redirect('templates', pid)

        # redirect('index')
    else:
        # form = templateform()
        form = templateform(request.POST)
    return render(request, 'presapp/newprescription.html', {'form': form, 'patientdetails': patientdetails})


def get_template(request, tid):
    #pid = presciptiontemplates.objects.raw("SELECT patientid from presciptiontemplates where templateid=%s",[tid])
    post = get_object_or_404(presciptiontemplates, templateid=tid)
    pid= post.patientid
    patientdetails = Patient.objects.get(patientid=pid)
    if request.method == "POST":
        form = templateform(request.POST, instance=post)
        messages.success(request, 'Prescription loaded')
        if form.is_valid():
            form.save(commit=False)
            Presciptiontemplates = presciptiontemplates()
            Presciptiontemplates.templateid = tid
            Presciptiontemplates.patientid = post.patientid
            Presciptiontemplates.savedate = datetime.now()
            Presciptiontemplates.template = form.cleaned_data.get('template')
            Presciptiontemplates.draft = form.cleaned_data.get('draft')
            Presciptiontemplates.save()
            messages.success(request, 'Prescription Saved Successfully')
        return redirect('templates',pid )
    else:
        form = templateform(instance=post)
    return render(request, 'presapp/viewtemplate.html', {'form': form, 'patientdetails': patientdetails})


def viewprescription(request, patid):
    patientdetails = Patient.objects.get(patientid=patid)
    prescription = presciptiontemplates.objects.filter(patientid=patid, draft=False).order_by('-savedate')
    drafts = presciptiontemplates.objects.filter(draft=True, patientid=patid).order_by('-savedate')
    draftcount = presciptiontemplates.objects.filter(draft=True, patientid=patid).count()
    return render(request, 'presapp/prescriptionlist.html', {'prescription': prescription, 'patientdetails': patientdetails, 'draftcount': draftcount, 'drafts': drafts})


def dashboard(request):
    patientCountall = Patient.objects.count()
    dataarray = []
    for month in range(1, 13):
        registrationsInPatient = Patient.objects.filter(rdate__month=month).count()
        registrationsInPatient = int(registrationsInPatient)
        dataarray.append(registrationsInPatient)
    return render(request, 'presapp/dashboard.html', {'patientCountall': patientCountall, 'dataarray': dataarray})


def loginview(request):
    form = loginForm()
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswrd']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('index')
            else:
                messages.error(request, 'User is not Active')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Error: User Does not exist')
    else:
        form = loginForm()
        return render(request, 'presapp/login.html', {'form': form})

def logoutview(request):
    messages.success(request, 'Logout Successful')
    logout(request)
    #form = loginForm(request.POST)
    next='/login'
    return redirect('login',next)


'''
def dashboardMonthData(request):
    dataarray = []
    for month in range(1,12):
        registrationsInPatient = Patient.objects.filter(rdate__month=month).count
        dataarray.append(registrationsInPatient)
    data = serializers.serialize('json', objectQuerySet, fields=(dataarray))

    return render(request, 'presapp/dashboard.html', {'data': data})

def pdfexport(request, tempid):
    response = HttpResponse(content_type='presapp/pdf')
    response['Content-Disposition'] = 'attachment; filename="Print.pdf"'
    buffer = BytesIO()
    data = presciptiontemplates.objects.filter(patientid=tempid)
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, data)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='presapp/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

'''
