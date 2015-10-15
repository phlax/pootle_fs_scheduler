import django.dispatch


status_changed = django.dispatch.Signal(providing_args=["status"])
