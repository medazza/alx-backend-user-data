#!/usr/bin/env python3
"""Session authenticating module.
"""
from typing import Tuple
import os
from flask import abort, jsonify, request

from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """POST /api/v1/auth_session/login
    Return:
      - JSON repr of a User object.
    """
    not_found_res = {"error": "no user found for this email"}
    em = request.form.get('email')
    if em is None or len(em.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    pwd = request.form.get('password')
    if pwd is None or len(pwd.strip()) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': em})
    except Exception:
        return jsonify(not_found_res), 404
    if len(users) <= 0:
        return jsonify(not_found_res), 404
    if users[0].is_valid_password(pwd):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401

@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """DELETE /api/v1/auth_session/logout
    Return:
      - Empty JSON object.
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})
