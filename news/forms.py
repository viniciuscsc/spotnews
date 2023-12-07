from django import forms


class NewCategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=200,
    )
