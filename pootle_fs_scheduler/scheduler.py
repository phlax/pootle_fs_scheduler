
import .signals


def handle_status(self):
    if status.has_changed:
        signal.send(sender=status.fs, status=status)



def schedule(self):
    pass
