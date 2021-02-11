from rest_framework import viewsets
from .serializers import WhoSerializer, ActivitySerializer
from .models import Who, Activity


class WhoViewSet(viewsets.ModelViewSet):
    queryset = Who.objects.all().order_by('who')
    serializer_class = WhoSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('end_date')
    serializer_class = ActivitySerializer
