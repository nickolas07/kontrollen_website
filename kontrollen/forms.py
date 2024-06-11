from django import forms


class Kontrolle(forms.Form):
    identifier = forms.CharField(label='identifier', widget=forms.HiddenInput(), required=False, localize=False)


class KontrolleErstellen(forms.Form):
    identifier = forms.CharField(label='identifier', widget=forms.HiddenInput(), required=False, localize=False)
    schule = forms.CharField(
        label='schule',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingSchule',
            'placeholder': 'Schule'
        }))
    schulart = forms.CharField(
        label='schulart',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingSchulart',
            'placeholder': 'Schulart'
        }))
    kurs = forms.ChoiceField(
        label='kurs',
        required=False,
        choices=[
            ('Grundkurs', 'Grundkurs'),
            ('Leistungskurs', 'Leistungskurs')
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'floatingKurs',
            'placeholder': 'Kurs'
        }))
    lehrer = forms.CharField(
        label='lehrer',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingLehrer',
            'placeholder': 'Lehrer'
        }))
    datum = forms.DateField(
        label='datum',
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'id': 'floatingDatum',
            'placeholder': 'Datum'
        }))
    kontrollen_art = forms.ChoiceField(
        label='kontrollen_art',
        required=False,
        choices=[
            ('Probe', 'Probe'),
            ('Test', 'Test')
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'floatingArt',
            'aria-label': 'Kontrollen-Art'
        }))
