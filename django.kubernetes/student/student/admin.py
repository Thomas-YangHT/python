from django.contrib import admin
from more_with_admin.examples import models
class DocumentAdmin(admin.ModelAdmin):
  pass
class CommentAdmin(admin.ModelAdmin):
  pass
admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.Comment, CommentAdmin)
