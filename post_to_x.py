import requests, os, tweepy, time

api_key = os.getenv("Vm67YLTZKK8YuEdsEOQ9A8fSm6LDEZ4y5q2FQ99hIM2PF2OhPD")
api_secret = os.getenv("A5rpZWar21KMDXvz")
access_token = os.getenv("1603109228687900675-5hU2AskV3cFckvHJMchPg6cS9Uaybg")
access_secret = os.getenv("WB4PhkDMeaO831OIyJdJkfZSVB39AHNfF1Mz4pv61QECd")

# Shoppy API
shoppy_key = os.getenv("SHOPPY_API_KEY")
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
