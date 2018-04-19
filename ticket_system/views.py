from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse;
from ticket_system.models import Ticket
from ticket_system.forms import TicketForm
from django.core.mail import send_mail
from django.conf import settings;



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
            ticket = form.save();


            ##### Send Email to user to confirm sending issue #####

            subject = "Message submitted successfully!";
            from_email = settings.EMAIL_HOST_USER;
            to_email = [ticket.ticket_user_email];
            messege = """

                    Thank you for contacting us !

                    Your issue has been recorded and you can track its status through this link

                    http://localhost:8000/tickets/track/""" + str(ticket.id);
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=messege, fail_silently=False);
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

    if(ticket.ticket_status):
        subject = "Issue Solved";
        from_email = settings.EMAIL_HOST_USER;
        to_email = [ticket.ticket_user_email];
        messege = """
            
            Thank you for contacting us !
            
            Your issue number #""" + str(ticket.id) + """ has been successfully resolved. """ ;
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=messege, fail_silently=False);

    return HttpResponseRedirect("/tickets/all");

##################################################

def track_ticket_view(request, ticket_id):

    ticket = Ticket.objects.get(id=ticket_id);

    context = {
        "ticket": ticket
    }
    return render(request, 'track_ticket.html', context);
