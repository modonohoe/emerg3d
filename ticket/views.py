from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import EnquiryTicket
from .forms import EnquiryTicketForm
from django.contrib.auth.decorators import login_required
from .constants import COUNTRY_CHOICES
from django.http import JsonResponse
from django.template.loader import render_to_string


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

    return render(request, 'ticket/ticket.html', {'form': form})


@login_required
def thank_you(request):
    context = {
        'user_name': request.user.username,
        'user': request.user
    }
    return render(request, 'ticket/thank_you.html', context)


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
    # Ensure the request is AJAX and method is POST
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        try:
            ticket = EnquiryTicket.objects.get(id=ticket_id, user=request.user)
            ticket.delete()
            return JsonResponse({"status": "success", "message": "Ticket deleted successfully."}, status=200)
        except EnquiryTicket.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Ticket not found."}, status=404)


@login_required
def get_ticket_data(request, ticket_id):
    ticket = get_object_or_404(EnquiryTicket, id=ticket_id,  user=request.user)
    form = EnquiryTicketForm(instance=ticket)
    form_html = render_to_string('edit_form.html', {'form': form}, request=request)

    return JsonResponse({'form_html': form_html})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(EnquiryTicket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = EnquiryTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your ticket has been updated successfully.')
            return JsonResponse({'success': True})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': error_messages})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})