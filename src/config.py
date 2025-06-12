"""
Configuration module for loading environment variables.
"""

import os

SETLISTFM_API_KEY = os.getenv("SETLISTFM_API_KEY")
SETLISTFM_API_BASE_URL = 'https://api.setlist.fm/rest/1.0'
