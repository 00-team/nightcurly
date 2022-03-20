# signals
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver

# models
from Account.models import Account

# threading
from threading import Thread

# utils
from utils.models import download_file

# webhooks
from utils.webhook.hooks import account_hook

DEL_KWARGS = {'save': False}


def account_profile(instance, status):
    try:
        picture = download_file(instance.picture_url)

        if picture:
            instance.picture.save('picture.jpg', picture)

        account_hook(instance, status)
    except Exception as e:
        print(e)


# media - profile picture
@receiver(pre_save, sender=Account)
def account_pre_save(sender, instance, **kwargs):
    try:
        try:
            old_instance = sender.objects.get(id=instance.id)
        except:
            old_instance = None

        try:
            if old_instance.picture != instance.picture:
                old_instance.picture.delete(**DEL_KWARGS)
        except:
            pass

        try:
            status = 'update' if old_instance else 'new'

            if not instance.picture_url:
                account_hook(instance, status)
                return

            if old_instance:
                if old_instance.picture_url == instance.picture_url and instance.picture:
                    return

            thread = Thread(target=account_profile, args=(instance, status))
            thread.start()

        except:
            pass

    except Exception as e:
        print(e)


@receiver(pre_delete, sender=Account)
def account_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        account_hook(instance, 'delete')
    except:
        pass