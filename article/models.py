from django.db import models
from DjangoUeditor.models import UEditorField


class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    content = UEditorField(u'内容', width=600, height=300, toolbars="full", imagePath="media/", filePath="media/",
                           upload_settings={"imageMaxSize": 1204000}, blank=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
