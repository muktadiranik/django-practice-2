from django import forms


class BilingualForm(forms.Form):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('tr', 'Turkish'),
    ]

    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        initial='en',
        widget=forms.Select(attrs={'class': 'form-select language-switch'}),
    )

    name_en = forms.CharField(max_length=100, label="Name", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email_en = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message_en = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label="Message")

    name_tr = forms.CharField(max_length=100, label="İsim", required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_tr = forms.EmailField(label="E-posta", required=False,
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message_tr = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label="Mesaj", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = kwargs.get('initial', {}).get('language', 'en')
        self.update_required_fields()

    def update_required_fields(self):
        for field_name in self.fields:
            if field_name.endswith(f'_{self.language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(('_en', '_tr')):
                self.fields[field_name].required = False
