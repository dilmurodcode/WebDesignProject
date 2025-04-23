from . import models
from rest_framework import serializers


class PortfolioSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Portfolio
        fields = (
            'id', 'poster', 'feat', 'url', 'specialization'
        )


class ProjectProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectProgress
        fields = (
            'id', 'image', 'title', 'order', 'portfolio'
        )


class PortfolioProjectProgressMixedSerializer(serializers.ModelSerializer):
    project_progresses = ProjectProgressSerializer(many=True)


    class Meta:
        model = models.Portfolio
        fields = (
            'id', 'poster', 'feat', 'url', 'specialization', 'project_progresses'
        )
