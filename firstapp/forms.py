# для работы с изображениями
from django import forms
from .models import Person
from .models import Image
from .models import File
from .models import VideoFile
from .models import AudioFile


class UserForm(forms.ModelForm):
    # name = forms.CharField(label="Имя клиента", widget=forms.TextInput(attrs={"class": "myfield"}))
    # age = forms.IntegerField(label="Возраст клиента", widget=forms.NumberInput(attrs={"class": "myfield"}))
    class Meta:
        model = Person
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class FileFrom(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'
