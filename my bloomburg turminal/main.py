from requests import *


STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon.com, Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = "99S7DSBJVS8MRV3M"
news_api_key = "abcf21649e804b3c9e07baad17f63fcf"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key

}



response = get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


#TODO 2. - Get the day before yesterday's closing stock price
db_yesterday_data = data_list[1]
db_yesterday_closing_price = db_yesterday_data["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diffrence = abs(float(yesterday_closing_price) - float(db_yesterday_closing_price))




#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (diffrence / float(yesterday_closing_price)) * 100





#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 0.1:
    news_params = {
        "apiKey" : news_api_key,
        "qInTitle": COMPANY_NAME,

    }
    news_response = get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted = [f"Headline: {article['title']}.\n Brief: {article['description']}" for article in three_articles]
print(formatted)

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

