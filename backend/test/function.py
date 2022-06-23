## --------------------------
## Login token for first login
## --------------------------
import secrets
def tokenGenrator():
    return secrets.token_urlsafe(32)