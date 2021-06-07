from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import cache_control

from ems.models import CompanyAdmin, EmployerData


def login(request):
    if 'admin_id' not in request.session:
        if request.method == 'POST':
            email = request.POST['email'].lstrip()
            password = request.POST.get('password').lstrip()

            log_user = CompanyAdmin.objects.filter(admin_email=email, admin_password=password).first()
            messages.info(request, "")
            if log_user:
                request.session['admin_id'] = log_user.admin_id
                return redirect('/employerDashboard')

            else:
                messages.info(request, "Invalid Credentials..")
                return redirect("/")

        else:
            return render(request, 'login.html')
    else:
        return redirect('/employerDashboard')
    return render(request, "login.html")

def register(request):
    if 'admin_id' not in request.session:
        if request.method == 'POST':
            email = request.POST['email'].lstrip()
            name = request.POST['fullname'].lstrip()
            password = request.POST.get('password').lstrip()
            messages.info(request, "")
            if email != "" or name != "" or password != "":
                admin_data = CompanyAdmin(admin_email = email, admin_name = name, admin_password = password)
                admin_data.save()
                messages.info(request, "Register successful..Do login!")
                return redirect('/')

            else:
                messages.info(request, "All fields are required..")
                return redirect("/registration")

        else:
            return render(request, 'registration.html')
    else:
        return redirect('/employerDashboard')
    return render(request, "registration.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    else:
        emp_data = EmployerData.objects.all()
        return render(request, "dashboard.html", {"emp_data": emp_data})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def emp_data_form(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            id = request.POST['id']
            email = request.POST['email'].lstrip()
            contact = request.POST['mobile'].lstrip()
            name = request.POST['name'].lstrip().upper()
            design = request.POST['design'].lstrip().upper()
            sal = request.POST['salary'].lstrip()
            messages.info(request, "")

            if id != "":
                if email != "" and contact != "" and name != "" and design != "" and sal != "":
                    emp = EmployerData.objects.get(id=id)
                    emp.name = name
                    emp.mobile = contact
                    emp.email = email
                    emp.design = design
                    emp.salary = sal
                    emp.save()
                    messages.info(request, "Employer updated successful!")
                    return redirect("employerDashboard")
                else:
                    messages.info(request, "All details are necessary..")
                    emp = EmployerData.objects.get(id=id)
                    return render(request, "empdataform.html", {"emp": emp})
            else:
                if email != "" and contact != "" and name != "" and design != "" and sal != "":
                    emp_data = EmployerData(name=name, mobile=contact, email=email, design=design, salary=sal)
                    emp_data.save()
                    messages.info(request, "Employer added successful!")
                    return redirect("employerDashboard")
                else:
                    messages.info(request, "All details are necessary..")

        return render(request, "empdataform.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    try:
        del request.session['admin_id']
    except KeyError:
        pass
    return redirect('/')


def emp_data_edit(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    else:
        emp = EmployerData.objects.get(id=id)
        return render(request, "empdataform.html", {"emp":emp})




def emp_data_delete(request,id):
    if 'admin_id' not in request.session:
        return redirect('/')
    else:
        emp = EmployerData.objects.get(id=id)
        emp.delete()
        messages.info(request, "Employer removed Successful!!")
        return redirect('employerDashboard')

