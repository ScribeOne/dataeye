from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import HutEye, ModelType, HutEyeRecord, Profile


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj=obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(ModelType)
admin.site.register(HutEye)
admin.site.register(HutEyeRecord)
admin.site.register(Profile)
