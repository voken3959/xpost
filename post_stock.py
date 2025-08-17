import os
import requests
import tweepy

# Load secrets from GitHub Actions
SHOPPY_API_KEY = os.getenv("Vm67YLTZKK8YuEdsEOQ9A8fSm6LDEZ4y5q2FQ99hIM2PF2OhPD")

TWITTER_CONSUMER_KEY = os.getenv("Fx0kmW6052W6t52bBKhJZ4mk2")
TWITTER_CONSUMER_SECRET = os.getenv("k12HmDVQkm3sJG0uAAt9RqW3DBgRirDzkbBpk1DjUDiDnBjDyY")
TWITTER_ACCESS_TOKEN = os.getenv("1603109228687900675-5hU2AskV3cFckvHJMchPg6cS9Uaybg")
TWITTER_ACCESS_SECRET = os.getenv("WB4PhkDMeaO831OIyJdJkfZSVB39AHNfF1Mz4pv61QECd")

# Setup Twitter
auth = tweepy.OAuth1UserHandler(
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)
twitter_api = tweepy.API(auth)

# Get Shoppy products
headers = {"Authorization": f"Bearer {SHOPPY_API_KEY}"}
resp = requests.get("https://shoppy.gg/api/v1/products", headers=headers)
products = resp.json()

# Example: only post about "Discord Nitro 1 Month"
for product in products:
    if "Nitro" in product["title"]:
        stock = product["stock"]
        price = product["price"]  # If set in Shoppy
        message = f"✨ {product['title']} – £{price}\n🎮 Only {stock} left!"
        
        twitter_api.update_status(message)
        print("Posted:", message)
