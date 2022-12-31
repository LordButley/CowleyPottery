from django.shortcuts import render, redirect, reverse
from .models import Commission
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
            return redirect(reverse('commissions_success'))
        else:
            messages.error(request, 'Request failed. Please ensure the form has been filled in correctly')
    else:
        form = CommissionForm

    context = {
        'form': form,
    }
    return render(request, "commissions/commissions.html", context)

def commissions_success(request):
    """ A view for the commissions success page """
    return render(request, "commissions/commissions_success.html")


def commissions_list(request):
    """ A view for the commissions list page """
    
    commissions = Commission.objects.all()

    context = {
        'commission_list':commissions,
    }

    return render(request, "commissions/commissions_list.html", context)
