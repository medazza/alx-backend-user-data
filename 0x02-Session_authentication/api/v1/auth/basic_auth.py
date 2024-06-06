#!/usr/bin/env python3
""" Basic auth module """

from .auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    pass
