from __future__ import absolute_import, unicode_literals
import os
from dotenv import load_dotenv

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(PROJECT_BASE_DIR, '.env'))