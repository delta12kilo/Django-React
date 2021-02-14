from rest_framework import permissions
from rest_framework.views import APIView
from .models import COntact
from .serializers import ContactSerializer
from django.core.mail import send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                +'\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'dk669709@gmail.com',
                ['dk669709@gmail.com'],
                fail_silently=False
            )
            contact =COntact(name=data['name'],
                            email=data['email'], 
                            subject=data['subject'],
                            message=data['message'])

            contact.save()
            return Response({'success': 'Mail has been sent'})

        except :
            return Response({'error': 'Message Failed :('})