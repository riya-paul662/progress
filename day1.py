print('----Welcome to the USD to INR Exchange tool----')
exchange_rate=94.95
usd_amount=float(input("enter amount in USD:"))
inr_amount=usd_amount * exchange_rate
print(f"${usd_amount} USD is exactly equal to ₹{inr_amount} INR")