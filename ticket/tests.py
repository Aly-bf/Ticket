
from django.test import TestCase
from django.urls import reverse
from ticket.models import Ticket
import ticket


# class TicketViewTest(TestCase):
#     def test_ticket_post_valid_data(self):
#         data = {
#             'subject': 'whatsapp',  
#             'description': 'whats app is filter',
#         }
#         response = self.client.post(reverse('ticket:ticket_list'), data)
#         self.assertEqual(response.status_code, 302)  
#         self.assertEqual(Ticket.objects.count(), 1)  


#     def test_ticket_get_request(self):
#         response = self.client.get(reverse('ticket:ticket'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'ticket/ticket.html') 



class TestTicket(TestCase):

    def setUp(self):
        self.ticket1 = Ticket.objects.create(subject='pintrest', description='good image in this')
        
    def test_ticket(self):
         response = self.client.get(reverse('ticket:ticket_list'))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'ticket/all_tickets.html')
         self.assertContains(response, 'pintrest')
         self.assertEqual(Ticket.objects.count(), 1)

    def test_delete_ticket(self):
        
        ticket_id = self.ticket1.id
        response = self.client.get(reverse('ticket:delete', args=[ticket_id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ticket.objects.count(), 0)
        self.assertFalse(Ticket.objects.filter(id= ticket_id).exists())

    # def test_ticket_detail_get(self):
    #     ticket_id = self.ticket1.id
    #     response = self.client.get(reverse('ticket:detail', args=[ticket_id]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ticket/ticket_detail.html')
    #     self.assertContains(response, 'pintrest')
        
