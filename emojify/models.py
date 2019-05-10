from django.db import models

class TextEmoji(models.Model):
    # Text Before
    text = models.CharField(max_length=280, null = False)

    # Text emojified
    emoji = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "{} - {}".format(self.text,self.emoji)
