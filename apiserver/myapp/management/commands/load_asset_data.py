from typing import Any, Optional

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        return super().handle(*args, **options)
