from datetime import datetime

date = datetime.now()
formatdate = date.strftime("%d %Y")
day = date.strftime("%A")
month = date.strftime("%B")

print(f"Seconds since january 1st 1970: {date.timestamp():,} or {date.timestamp():e} on scientific notation but it's more easy to say {month} {day} {formatdate}")
