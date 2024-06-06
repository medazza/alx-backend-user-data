#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authorithation"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """current user"""
        return None
