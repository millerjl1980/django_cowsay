from django.forms import modelform_factory
from cowsay.models import Cow

TextForm = modelform_factory(Cow, exclude=[])