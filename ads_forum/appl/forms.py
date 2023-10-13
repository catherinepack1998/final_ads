from django.forms import ModelForm
from .models import AdResponses, Ads

class AddAdForm(ModelForm):
    class Meta:
        model = Ads
        fields = ['heading', 'category', 'content', 'text']

class AddAdResponse(ModelForm):
    class Meta:
        model = AdResponses
        fields = ['response_text']
