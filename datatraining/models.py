from django.db import models


# Create your models here.
class File(models.Model):
    excel = models.FileField(upload_to='files/excels/')
    upload = models.DateField(null=True)
    keterangan = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.excel.delete()
        super().delete(*args, **kwargs)
