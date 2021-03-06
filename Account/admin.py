from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Account, BotUser, TwitterAccount


admin.site.unregister(User)


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', '_fullname',
        'lang', 'total_invites', 'inviter',
        'invites_counter', 'is_admin',
    )
    readonly_fields = (
        'user_id', 'lang', 'invite_hash',
        'has_logedin', '_fullname'
    )
    list_filter = ('is_admin', 'lang', 'invites_counter')
    search_fields = ('user_id', 'invite_hash')

    fieldsets = (
        ('Data', {'fields': ('_fullname', 'fullname', 'is_admin')}),
        ('Invites', {'fields': ('total_invites', 'invites_counter', 'inviter')}),
        ('Details', {
            'fields': ('user_id', 'invite_hash', 'lang', 'has_logedin')
        }),
    )

    @admin.display
    def has_logedin(self, obj):
        try:
            url = f'/admin/Account/account/{obj.account.id}/change/'
            return format_html(f'<a href="{url}">{obj.account}</a>')
        except:
            return 'No'


@admin.action(description='Participated')
def participated(modeladmin, request, queryset):
    queryset.update(participated=True)


@admin.action(description='No Participated')
def no_participated(modeladmin, request, queryset):
    queryset.update(participated=False)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'telegram_id', 'username',
        'has_wallet', 'participated', 'pic'
    )
    readonly_fields = ('pic', 'has_wallet')
    search_fields = ('username', 'telegram_id')
    list_filter = ('participated', )
    actions = (participated, no_participated)

    fieldsets = (
        ('Info', {
            'fields': ('telegram_id', 'username', 'wallet', 'participated')
        }),
        ('Relation', {
            'fields': ('user', 'bot_user')
        }),
        ('Photo', {
            'fields': ('picture_url', 'picture', 'pic')
        }),
    )

    @admin.display(boolean=True, ordering='-wallet')
    def has_wallet(self, obj):
        return bool(obj.wallet)

    @admin.display
    def pic(self, obj):
        if obj._picture:
            return format_html((
                f'<img src="{obj._picture}" '
                'height="121" style="border-radius:7px" />'
            ))

        return 'None'


@admin.register(TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', '_nickname', 'username',
        'account', 'followers', 'pic'
    )
    readonly_fields = (
        '_nickname', 'account', 'access_token',
        'expires_in', 'pic', 'user_id', '_description'
    )

    fieldsets = (
        ('Info', {
            'fields': (
                '_nickname', 'nickname', 'username',
                'followers', 'followings', 'tweets',
                'description', '_description'
            )
        }),
        ('picture', {'fields': ('picture_url', 'picture')}),
        ('Details', {
            'fields': (
                'account', 'access_token',
                'expires_in', 'user_id', 'pic'
            )
        }),
    )

    @admin.display
    def pic(self, obj):
        if obj._picture:
            return format_html((
                f'<img src="{obj._picture}" '
                'height="121" style="border-radius:7px" />'
            ))

        return 'None'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ('account', )

    fieldsets = (
        (None, {'fields': ('account', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
