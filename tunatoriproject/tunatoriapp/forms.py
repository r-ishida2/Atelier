from django.forms import ModelForm
from .models import Publish, Reply

class PublishCreationForm(ModelForm):
    class Meta:
        model = Publish
        fields = ('title', 'detail', 'image')

class ReplyCreationForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('rating', 'comment')