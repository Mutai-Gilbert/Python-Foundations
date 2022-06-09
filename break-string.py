# HINT: modify the headlines list to verify your loop works with different inputs
from operator import ne


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for items in headlines:
    news_ticker += items + " " #adding the headlines into the array sticker
    if len(news_ticker) >=140:
        news_ticker = news_ticker[:140] #here we are truncating the characters that exceed 140
        break

print(news_ticker)