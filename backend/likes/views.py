from django.shortcuts import render
from rest_framework import viewsets
from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
