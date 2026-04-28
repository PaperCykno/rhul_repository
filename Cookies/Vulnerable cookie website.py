from flask import Flask, request, make_response
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

app = Flask(__name__)

KEY = os.urandom(16)

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len])*pad_len

def unpad(data):
    return data[:-data[-1]]

def encrypt_cookie(data):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(data.encode()))
    return base64.b64encode(iv + ct).decode()

def decrypt_cookie(cookie):
    raw = base64.b64decode(cookie)
    iv = raw[:16]
    ct = raw[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct))
    return pt.decode()

@app.route("/")
def index():
    role = "role=user"
    cookie = encrypt_cookie(role)
    resp = make_response("Logged in as user")
    resp.set_cookie("session", cookie)
    return resp

@app.route("/admin")
def admin():
    cookie = request.cookies.get("session")
    if not cookie:
        return "No session"

    try:
        data = decrypt_cookie(cookie)
        if "role=admin" in data:
            return "FLAG: RHUL{cbc_needs_integrity}"
        else:
            return "Access denied"
    except:
        return "Invalid cookie"