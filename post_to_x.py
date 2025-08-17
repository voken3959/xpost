import requests, os, tweepy, time


auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Load secrets from GitHub Actions
SHOPPY_API_KEY = os.getenv("Vm67YLTZKK8YuEdsEOQ9A8fSm6LDEZ4y5q2FQ99hIM2PF2OhPD")
TWITTER_CONSUMER_KEY = os.getenv("Fx0kmW6052W6t52bBKhJZ4mk2")
TWITTER_CONSUMER_SECRET = os.getenv("k12HmDVQkm3sJG0uAAt9RqW3DBgRirDzkbBpk1DjUDiDnBjDyY")
TWITTER_ACCESS_TOKEN = os.getenv("1603109228687900675-5hU2AskV3cFckvHJMchPg6cS9Uaybg")
TWITTER_ACCESS_SECRET = os.getenv("WB4PhkDMeaO831OIyJdJkfZSVB39AHNfF1Mz4pv61QECd")
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

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
