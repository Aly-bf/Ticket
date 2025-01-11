from django.shortcuts import render, redirect, get_object_or_404
from .forms import TicketForm, MessageForm
from .models import Ticket, Message
import pandas as pd
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import TicketSerializers

@login_required
def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            form.save()
            return redirect('ticket:ticket_list')
    form = TicketForm()
    return render(request, 'ticket/ticket.html', {'form': form})

@login_required
def ticket_list(request):
    if request.user.is_superuser:
        tickets = Ticket.objects.all()
        df_ticket = pd.DataFrame(tickets.values('subject'))
        count = len(df_ticket)
    else:
        tickets = Ticket.objects.filter(user=request.user)
        count = tickets.count()
    return render(request, 'ticket/all_tickets.html', {'tickets': tickets, 'count':count})


def delete_ticket(request, pk):
    tickets = get_object_or_404(Ticket, id=pk)
    tickets.delete()
    return redirect('ticket:ticket_list')


def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    messages = ticket.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)  
            new_message.ticket = ticket  
            new_message.save()  
            return redirect('ticket:detail', pk=ticket.id)  
    else:
        form = MessageForm()

    return render(request, 'ticket/ticket_detail.html', {
        'ticket': ticket,
        'messages': messages,  
        'form': form,
    })
    

class TicketList(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers