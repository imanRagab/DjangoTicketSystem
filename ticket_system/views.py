from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from ticket_system.models import Ticket
from ticket_system.forms import TicketForm


def all_tickets_view(request):
   all_tickets = Ticket.objects.order_by('ticket_status')
   context = {
       "tickets":all_tickets
   }
   return render(request,'all_tickets.html',context)

################################################

def add_ticket_view(request):

    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/tickets/all")
    context = {
        "form":form,
    }
    return render(request,"ticket_form.html",context)

##################################################

def edit_ticket_view(request, ticket_id):
    obj = Ticket.objects.get(id = ticket_id)
    form = TicketForm(instance=obj)

    if request.method == "POST":
        form = TicketForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tickets/all')

    context = {
        "form":form
    }
    return render(request,'ticket_form.html',context)