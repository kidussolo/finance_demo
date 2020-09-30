from rest_framework import serializers
import demo import models

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Journal
        fields = '__all__'