from django import forms
# from .models import Survey


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()


# class SurveyForm(forms.Form):
#     class Meta:
#         model   = Survey
#         fields  =['name' ,'subject']
