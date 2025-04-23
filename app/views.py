from rest_framework import generics
from . import models
from . import serializers


class PortfolioAPIView(generics. ListAPIView):
    queryset = models.Portfolio.objects.filter()
    serializer_class = serializers.PortfolioSerializers


class PortfolioProjectProgressMixedAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.PortfolioProjectProgressMixedSerializer
    pagination_class = None

    def get_object(self):
        pk = self.kwargs.get('pk')

        return models.Portfolio.objects.filter(id=pk).prefetch_related('project_progresses').first()