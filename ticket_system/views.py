from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from ticket_system.models import Ticket
from ticket_system.forms import TicketForm


def all_tickets_view(request):
   all_tickets = Ticket.objects.order_by('ticket_status');
   context = {
       "tickets":all_tickets
   }
   return render(request,'all_tickets.html',context);

################################################

def add_ticket_view(request):

    form = TicketForm();
    if request.method == "POST":
        form = TicketForm(request.POST);
        if form.is_valid():
            form.save();
            ### Send Email to user to confirm sending issue #####
            return HttpResponseRedirect("/tickets/all");
    context = {
        "form":form,
    }

    return render(request,"ticket_form.html",context);

##################################################

def change_status_view(request, ticket_id):


    ticket = Ticket.objects.get(id = ticket_id);

    ####Toggle Status######

    ticket.ticket_status = 0 if ticket.ticket_status else 1;

    ticket.save();

    ### Send Email to notify user that case is resolved ######





    return HttpResponseRedirect("/tickets/all");

##################################################

def track_ticket_view(request, ticket_id):

    ticket = Ticket.objects.get(id=ticket_id);

    context = {
        "ticket": ticket
    }
    return render(request, 'track_ticket.html', context);
