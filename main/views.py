from django.shortcuts import render
from oauthlib.uri_validate import query
from rest_framework import viewsets
from rest_framework.response import Response

from transformers import pipeline

from .models import IgModel
from.serializers import IgSerializer

# Create your views here.

class IgViewSet(viewsets.ModelViewSet):
    queryset = IgModel.objects.all()
    serializer_class = IgSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        saved_instance = serializer.instance
        user_message = saved_instance.message
        sender_id = saved_instance.sender

        classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

        # labels
        candidate_labels = ["greeting","make an appointment", "information about appointment date",
                            "other information about payment", "complain", "cancel an appointment","email address","other"]

        result = classifier(user_message, candidate_labels)
        print(f"intent classified: {result['labels'][0]} with score {result['scores'][0]:.3f}")
        return Response({
            'message':user_message,
            'classified_intent':result['labels'][0],
            'saved_id':saved_instance.id,
            'sender_id':sender_id
        })
