# types
from telegram import Chat, Update

# exceptions
from telegram.error import BadRequest, Unauthorized

# user
from .user import User

# keyboards
from .keyboards import help_keyboard, login_keyboard
from .keyboards import join_keyboard, invite_keyboard

# decorators
from .decorators import user_data

# data
from .data import get_chats, update_chats
from .data import markdown_free

# langs
from .langs import CONTNET

JOIN_PHOTO = 'AgACAgQAAxkBAAICT2IUoWhe2dqMs5JH4KQOsVUIYBXnAAJWuTEbX9OgUMou1QABxjrs5wEAAwIAA20AAyME'
INVITE_PHOTO = 'AgACAgQAAxkBAAICjWIUvJR2Ij73vIEeNU4VHJaH_JVDAALUtzEbTt2oUH7o1bYu7AtdAQADAgADeQADIwQ'


@user_data
def login(update: Update, lang, **kwargs):
    chat = update.effective_chat

    chat.send_message(
        CONTNET[lang]['login'],
        reply_markup=login_keyboard(lang),
    )


def user_joined(user: Chat) -> list[Chat]:
    chats = get_chats()
    bot = user.bot
    user_chats = []

    for chat in chats:
        try:
            res = bot.get_chat_member(chat, user.id)
            if res.status in ['left', 'kicked']:
                chat = bot.get_chat(chat)
                user_chats.append(chat)
        except Unauthorized:
            chats.remove(chat)
            update_chats(chats)
        except BadRequest:
            chats.remove(chat)
            update_chats(chats)

    return user_chats


def check_inviter(user_chats: list[Chat], bot_user: User):
    if not bot_user.inviter or bot_user.CFI:
        return

    try:
        if not user_chats:
            the_inviter = User(bot_user.inviter.user_id)
            old_total_invites = the_inviter.total_invites
            the_inviter.increase_invites()
            new_total_invites = the_inviter.total_invites

            if new_total_invites > old_total_invites:
                bot_user.CFI_done()
    except:
        pass


@user_data
def join_chats(update: Update, bot_user, lang, **kwargs):
    user = update.effective_user
    user_chats = user_joined(user)
    chat = update.effective_chat

    check_inviter(user_chats, bot_user)

    if user_chats:
        chat.send_photo(
            JOIN_PHOTO,
            caption=CONTNET[lang]['join_chats'],
            reply_markup=join_keyboard(user_chats, lang),
        )
    else:
        chat.send_photo(
            JOIN_PHOTO,
            caption=CONTNET[lang]['joined_chats'],
        )


@user_data
def update_join_chats(update: Update, bot_user, lang, **kwargs):
    query = update.callback_query
    user = update.effective_user
    user_chats = user_joined(user)

    check_inviter(user_chats, bot_user)

    if user_chats:
        return

    query.message.edit_caption(
        CONTNET[lang]['join_complete'],
        reply_markup=None,
    )


@user_data
def invite(update: Update, bot_user: User, lang, **kwargs):
    user = update.effective_user
    chat = update.effective_chat
    bot_username = user.bot.username
    enough_invites = bot_user.total_invites >= 3

    user_link = f'https://t.me/{bot_username}?start=invite-{bot_user.invite_hash}'

    text = CONTNET[lang]['invites']
    text = text.format(user_link, bot_user.total_invites)

    user.send_message(text)

    user.send_photo(
        INVITE_PHOTO,
        CONTNET[lang]['invite_banner'],
        reply_markup=invite_keyboard(user_link, lang),
    )

    if enough_invites:
        chat.send_message(CONTNET[lang]['enough_invites'])


@user_data
def start(update: Update, context, lang, **kwargs):

    user = update.effective_user

    user.send_message(CONTNET[lang]['start'])
    user.send_message(CONTNET[lang]['help'], reply_markup=help_keyboard(lang))

    try:
        arg = context.args[0]

        if arg == 'login':
            user.send_message(
                CONTNET[lang]['external_login'],
                reply_markup=login_keyboard(lang),
            )

    except:
        pass


@user_data
def help_cmd(update: Update, lang, **kwargs):
    user = update.effective_user
    user.send_message(CONTNET[lang]['help'], reply_markup=help_keyboard(lang))


@user_data
def help_callback(update: Update, **kwrags):
    query = update.callback_query

    match query.data[5:]:
        case 'join':
            join_chats(update=update, **kwrags)
        case 'invite':
            invite(update=update, **kwrags)
        case 'login':
            login(update=update, **kwrags)
        case _:
            return
