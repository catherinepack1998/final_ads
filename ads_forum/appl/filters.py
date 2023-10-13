from django_filters import FilterSet
from .models import *
class ResponseFilter(FilterSet):
    class Meta:
        model = AdResponses
        fields = ('ad_id_id', 'user_id_id', 'response_text')