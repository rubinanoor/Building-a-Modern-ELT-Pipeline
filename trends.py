# 25280028
# Rubina Noor

def fetch_google_trends(keywords):
        
    from pytrends.request import TrendReq
    import matplotlib.pyplot as plt
    import time

    # initialize Google Trends Request object
    pt = TrendReq(hl = 'en-US', tz = 360)

    # set the keyword & timeframe
    pt.build_payload(keywords, timeframe="all")

    # Optional small delay to reduce risk of 429
    time.sleep(5)

    # get the interest over time
    iot = pt.interest_over_time()


    print(iot.head())

  

    # save data to csv and json
    iot.to_csv("data/raw/google_trends_raw.csv")
    iot.to_json("data/raw/google_trends_raw.json", orient="records")
    print("DATA SAVED TO data/raw/")

    return iot