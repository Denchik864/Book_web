from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)


class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager


class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()


class Image(models.Model):
    title = models.CharField(max_length=100, null=False,
                             verbose_name="Описание изображения", )
    image = models.ImageField(upload_to='images',
                              verbose_name="Файл с изображением",
                              null=True, blank=True)
    obj_img = models.Manager()

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100, verbose_name="Описание файла", )
    file = models.FileField(upload_to='files', verbose_name="Файл PDF", null=True, blank=True)

    def __str__(self):
        return self.title


class VideoFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Описание файла", )
    file = models.FileField(upload_to='videos', verbose_name="Видеофайл", null=True, blank=True)
    obj_video = models.Manager()

    def __str__(self):
        return self.title

class AudioFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Описание файла",)
    file = models.FileField(upload_to='audios', verbose_name="Аудиофайл", null=True, blank=True)
    obj_audio = models.Manager()

    def __str__(self):
        return self.title
