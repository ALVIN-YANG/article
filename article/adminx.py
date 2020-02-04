import xadmin
from xadmin.views import ModelAdminView
from xadmin.filters import DateFieldListFilter
from .models import Article


class ArticleModelAdmin(ModelAdminView):
    list_display = 'title', '_content'
    style_fields = {'content': 'ueditor'}

    def _content(self, instance):
        return instance.title[:10]
    _content.short_description = '内容'


xadmin.site.register(Article, ArticleModelAdmin)
