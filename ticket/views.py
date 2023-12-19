from django.shortcuts import render, redirect
from .forms import EnquiryTicketForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def create_enquiry_ticket(request):
    if request.method == 'POST':
        form = EnquiryTicketForm(request.POST)
        if form.is_valid():
            enquiry_ticket = form.save(commit=False)
            enquiry_ticket.user = request.user 
            enquiry_ticket.save()
            return redirect('thank_you')
    else:
        form = EnquiryTicketForm()

    return render(request, 'enquiry_ticket_form.html', {'form': form})

@login_required
def thank_you(request):
    return render(request, 'thank_you.html')