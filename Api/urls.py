from django.urls import include, path

from .views import account, bot, collection, tools


urlpatterns = [

    # Accounts
    path(
        'account/',
        include([
            # telegram
            path('telegram_callback/', account.telegram_callback),

            # twitter
            path('twitter_auth/', account.twitter_auth),
            path('twitter_callback/', account.twitter_callback),
            path('disconnect_twitter/', account.disconnect_twitter),

            # main
            path('logout/', account.logout),
            path('get/', account.get_account),
            path('update/', account.update),
            path('general_info/', account.general_info),
            path('messages/', account.get_messages),
        ]),
    ),

    # Bot Private Api
    path(
        'bot/',
        include([
            path('user_status/', bot.user_status),
            path('get_bot_user/', bot.get_bot_user),
            path('update_inviter/', bot.update_inviter),
        ]),
    ),

    # Collection
    path(
        'collection/',
        include([
            path('owners/', collection.get_owners),
            path('owner/', collection.get_owner),
            path('faqs/', collection.get_faqs),
        ]),
    ),

    # Tools
    path(
        'tools/',
        include([
            path('wallets/', tools.wallets),
        ]),
    ),
]
