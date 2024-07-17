from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, ChatRoom, Message

class MyUserAdmin(UserAdmin):
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'profile_picture')}),
    )

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(ChatRoom)
admin.site.register(Message)