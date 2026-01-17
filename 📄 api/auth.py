VALID_TOKENS = {
"token_basic": "basic",
"token_pro": "pro",
}




def check_token(token: str) -> str:
if token not in VALID_TOKENS:
raise PermissionError("Invalid subscription")
return VALID_TOKENS[token]


from fastapi import FastAPI, Header
from .auth import check_token


app = FastAPI()


@app.get("/secrets")
def list_secrets(x_api_key: str = Header(...)):
tier = check_token(x_api_key)
return {"tier": tier, "secrets": ["API_KEY", "DB_PASS"]}
