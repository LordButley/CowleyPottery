from django.shortcuts import render
from .forms import CommissionForm
from django.contrib import messages


# Create your views here.

def commissions_form_view(request):
    """ A view to see the commissions page and form """

    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request sent successfully')
        else:
            messages.error(request, 'Request failed. Please ensure the form has been filled in correctly')
    else:
        form = CommissionForm

    context = {
        'form' : form,
    }
    return render(request, "commissions/commissions.html", context)

