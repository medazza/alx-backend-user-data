#!/usr/bin/env python3
"""  Encrypting passwords module """
import bcrypt


def hash_password(password: str) -> bytes:
    """function that expects one string argument name password
        and returns a salted"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """doc doc doc"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
