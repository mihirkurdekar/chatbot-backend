from django import forms
from rest_framework import serializers

class FileUploadForm(forms.Form):
    file = forms.FileField()

class EntitySerializer(serializers.Serializer):
    start = serializers.IntegerField()
    end = serializers.IntegerField()

class CommonExampleSerizalier(serializers.Serializer):
    text = serializers.CharField()
    intent = serializers.CharField()
    entities = serializers.ListField(
        child = EntitySerializer()
    )

class RasaEntity(serializers.Serializer):
    common_examples = serializers.ListField(
        child= CommonExampleSerizalier()
    )

class TrainingObjectSerializer(serializers.Serializer):
    question = serializers.CharField()
    answer =  serializers.CharField()
    intent = serializers.CharField()
    entities = serializers.ListField(
        child = serializers.CharField()
    )