#from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()
admin.site.site_header = 'Coach ME'


@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = ('pk', 'username', 'email', 'date_joined')
    list_display_links = ('username',)
    readonly_fields=('date_joined', 'last_login')

#class UserAdmin(admin.UserAdmin):
#     add_form = CustomUserCreationForm
#     #form = CustomUserChangeForm
#    model = User
#     list_display = ('pk', 'email', 'username')
#     #list_select_related = ('city',)
#     # fieldsets = (
#     #     (None, {'fields': ('email', 'password')}),
#     #     ('Personal info', {'fields': ('date_of_birth',)}),
#     #     ('Permissions', {'fields': ('is_admin',)}),
#     # )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('city',),
#         }),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('city',),
#         }),
#     )
#     #filter_vertical = ('city',)




#admin.site.register(User, UserAdmin)
