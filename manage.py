#!/usr/bin/env python
import os
import sys

# Pythonista3用の読み込み設定
sys.path.append("/private/var/mobile/Containers/Shared/AppGroup/F7C23EA3-26EE-49B5-977E-29D0F78748A8/Pythonista3/Documents/djangogirls")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
