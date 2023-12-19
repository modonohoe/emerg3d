from django.contrib import messages
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

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(EnquiryTicket, id=ticket_id, user=request.user)

    if request.method == 'POST':
        form = EnquiryTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            if ticket.status != 'pending':
                messages.error(request, 'This ticket cannot be edited as it has been accepted.')
                return redirect('profile')

            form.save()
            messages.success(request, 'Your ticket has been updated')
            return redirect('profile')
    else:
        if ticket.status != 'pending':
            messages.error(request, 'This ticket cannot be edited as it has been accepted.')
            return redirect('profile')

        form = EnquiryTicketForm(instance=ticket)

    return render(request, 'edit_ticket_form.html', {'form': form})


@login_required
def delete_ticket(request, ticket_id):
    ticket = EnquiryTicket.objects.get(id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('profile')  # Or wherever appropriate
    return render(request, 'delete_ticket_confirm.html', {'ticket': ticket})
