import requests, os, tweepy, time

api_key = os.getenv("5xDYet2k92ewaDxS8zGFPmT0w")
api_secret = os.getenv("9eL8KDwFmBodooVOt0OgKyY5u51rZF1AnTQo0epSAf1XW1CVxb")
access_token = os.getenv("1603109228687900675-5hU2AskV3cFckvHJMchPg6cS9Uaybg")
access_secret = os.getenv("WB4PhkDMeaO831OIyJdJkfZSVB39AHNfF1Mz4pv61QECd")

# Shoppy API
shoppy_key = os.getenv("Vm67YLTZKK8YuEdsEOQ9A8fSm6LDEZ4y5q2FQ99hIM2PF2OhPD")
headers = {"Authorization": shoppy_key}

# Get products
r = requests.get("https://shoppy.gg/api/v1/products", headers=headers)
products = r.json()

# Hashtags to use
tags = ["#Deals", "#CheapSubs", "#LifetimeAccess", "#EverPass"]

for product in products:
    name = product.get("title")
    stock = product.get("stock", "N/A")
    price = product.get("price")
    
    message = f"🔥 {name}\n💰 £{price}\n📦 Stock: {stock} left\n\n{' '.join(tags)}"
    
    try:
        api.update_status(message)
        print("Posted:", message)
    except Exception as e:
        print("Error posting:", e)
    
    # avoid rate limit (pause between tweets)
    time.sleep(15)
