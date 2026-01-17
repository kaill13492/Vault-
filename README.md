# 🔐 Python Vault

Przykładowe repozytorium w Pythonie pokazujące, jak zbudować **prosty vault** (sejf) do bezpiecznego przechowywania sekretów (np. haseł, tokenów API, kluczy prywatnych) z użyciem szyfrowania.

Projekt ma charakter **edukacyjny**, ale opiera się na dobrych praktykach.

---

## 📌 Funkcje

* 🔑 Szyfrowanie danych przy użyciu hasła master
* 🧂 Automatyczne generowanie soli
* 🔒 Bezpieczne przechowywanie danych w pliku
* ♻️ Dodawanie, odczyt i usuwanie sekretów
* 🐍 Czysty, czytelny Python

---

## 📂 Struktura projektu

```text
python-vault/
│
├── vault/
│   ├── __init__.py
│   ├── crypto.py        # logika szyfrowania
│   ├── storage.py       # zapis/odczyt danych
│   └── vault.py         # główna logika vaulta
│
├── tests/
│   └── test_vault.py
│
├── main.py              # CLI demo
├── requirements.txt
└── README.md
```

---

## ⚙️ Wymagania

* Python **3.10+**
* biblioteka `cryptography`

```bash
pip install cryptography
```

---

## 🔐 Jak działa vault

1. Użytkownik podaje **hasło master**
2. Z hasła generowany jest klucz (PBKDF2 + salt)
3. Dane są szyfrowane algorytmem **Fernet (AES)**
4. Zaszyfrowany vault zapisywany jest do pliku JSON

---

## 🧠 Przykładowa implementacja

### `crypto.py`

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt(data: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(data.encode())


def decrypt(token: bytes, key: bytes) -> str:
    return Fernet(key).decrypt(token).decode()
```

---

### `vault.py`

```python
import json
import os
from .crypto import derive_key, encrypt, decrypt

class Vault:
    def __init__(self, password: str, path: str = "vault.json"):
        self.path = path
        self.salt = os.urandom(16)
        self.key = derive_key(password, self.salt)
        self.data = {}

    def add_secret(self, name: str, value: str):
        self.data[name] = encrypt(value, self.key).decode()

    def get_secret(self, name: str) -> str:
        return decrypt(self.data[name].encode(), self.key)

    def save(self):
```
