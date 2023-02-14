from django.contrib import admin
from blog.models import Article, Person, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Person)
admin.site.register(Comment)

