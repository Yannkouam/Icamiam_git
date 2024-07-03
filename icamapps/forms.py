from django import forms

class CreateNewlist(forms.Form):
    Prenom = forms.CharField(label="Prenom", max_length=200)
    Nom = forms.CharField(label='Nom', max_length=200)
    Email = forms.EmailField(label='Mail')

class PanierForm(forms.Form):
    # Ajoutez des champs ici en fonction des besoins de votre panier
    pass