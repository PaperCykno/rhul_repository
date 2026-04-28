from flask import Flask, request, make_response
import base64

app = Flask(__name__)

@app.route("/")
def index():
    role = "role=user"
    encoded = base64.b64encode(role.encode()).decode()

    resp = make_response("Logged in as user")
    resp.set_cookie("session", encoded)
    return resp


@app.route("/admin")
def admin():
    cookie = request.cookies.get("session")

    if not cookie:
        return "No session"

    try:
        decoded = base64.b64decode(cookie).decode()
        print("Decoded cookie:", decoded)

        if "role=admin" in decoded:
            return "FLAG: RHUL(never_trust_client)"
        else:
            return "Access denied"
    except:
        return "Invalid cookie"


if __name__ == "__main__":
    app.run(debug=True)