import hashlib


# symulacja bazy kluczy (w realu: API / backend)
VALID_LICENSES = {
"VAULT-PRO-2026": "pro",
"VAULT-ENT-2026": "enterprise",
}




def verify_license(key: str) -> str | None:
return VALID_LICENSES.get(key)
