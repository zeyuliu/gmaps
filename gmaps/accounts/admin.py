from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import WebUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = WebUser
        fields = ('email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password 2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = WebUser

    def clean_password(self):
        # regardless of what user provides, return initial value.
        # Done here rather than on the field, because the field does not have acces
        # to the initial value
        return self.initial["password"]

class WebUserAdmin(UserAdmin):
    # Forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(WebUser, WebUserAdmin)
admin.site.unregister(Group)

