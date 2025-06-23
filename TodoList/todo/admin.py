from django.contrib import admin

from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('no', 'todo_title', 'todo_content', 'todo_status', 'todo_is_completed', 'todo_created_at', 'todo_updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    actions = ('make_completed', 'delete_selected')

    @admin.display(description='제목')
    def todo_title(self, obj):
        return obj.title

    @admin.display(description='내용')
    def todo_content(self, obj):
        return obj.content[:10] + ('...' if len(obj.title) > 10 else '')
    
    @admin.display(description='상태')
    def todo_status(self,obj):
        return obj.get_status_display()
    
    @admin.display(boolean=True, description='완료여부')
    def todo_is_completed(self, obj):
        return obj.is_completed

    @admin.display(description='작성일')
    def todo_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')

    @admin.display(description='수정일')
    def todo_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    
    @admin.action(description='선택 완료 처리')
    def make_completed(self, request, queryset):
        queryset.update(status='DONE', is_completed=True)

    @admin.action(description='선택 삭제 처리')
    def delete_selected(self, request, queryset):
        queryset.delete()