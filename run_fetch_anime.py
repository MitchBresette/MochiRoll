import os
import django
from anime.utils import fetch_and_cache_anime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # adjust if your settings are elsewhere
django.setup()


#---- RUN fetch anime ----
fetch_and_cache_anime()
