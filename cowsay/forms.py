# from django import forms
from django.forms import modelform_factory
from cowsay.models import Cow

# class TextForm(forms.Form):
#    class Meta:
#         model = Cow
#         fields = ('text')

TextForm = modelform_factory(Cow, exclude=['output'])