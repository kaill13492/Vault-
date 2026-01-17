from datetime import datetime


APY = 0.05 # 5%
SECONDS_IN_YEAR = 365 * 24 * 60 * 60




def calculate_interest(balance: float, last_ts: float) -> tuple[float, float]:
now = datetime.utcnow().timestamp()
elapsed = now - last_ts


interest = balance * APY * (elapsed / SECONDS_IN_YEAR)
return interest, now
