from rest_framework import serializers
from .models import TextEmoji


class TextEmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEmoji
        fields = ("text", "emoji")