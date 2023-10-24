from django.contrib import admin
from . import models

# Register your models here.
class PostPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author' ,'status')
    list_display_links = ('id', 'title', 'author','status')
    list_filter = ('id','title','author', 'status' )
    search_fields = ( 'id','title', 'author','status' )


    
# 포스트를 관리자페이지와 연결
admin.site.register(models.PostPlan,PostPlanAdmin) 