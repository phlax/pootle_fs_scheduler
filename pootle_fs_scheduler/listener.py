from django.dispatch import receiver

from pootle_fs import ProjectFS

from .signals import status_changed


@receiver(pre_save, sender=ProjectFS)
def status_changed_handler(sender, found):
    # get the project config for conflict status
    pass
