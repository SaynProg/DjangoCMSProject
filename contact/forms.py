from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=50)
  email_address = forms.EmailField(max_length=150)
  subject = forms.CharField(max_length=150)
  text = forms.CharField(widget=forms.Textarea, max_length=4000)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'
    self.fields['name'].widget.attrs['placeholder'] = "Ваше ім'я"
    self.fields['email_address'].widget.attrs['placeholder'] = "Ваша електронна пошта"
    self.fields['subject'].widget.attrs['placeholder'] = "Тема"
    self.fields['text'].widget.attrs['placeholder'] = "Текст"