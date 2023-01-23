from bs4 import BeautifulSoup
import pandas as pd 
import requests
event_name=list()
event_date_time=list()

topic_url = "https://events.microsoft.com/en-us/allevents/?language=English&clientTimeZone=1&view=grid"
response = requests.get(topic_url)
restext = response.text
soup = BeautifulSoup(restext,"html5lib")
target_class_name = "c-heading-6"
tags_name=soup.find_all("h3",class_=target_class_name)
for i in range(len(tags_name)):
      if tags_name[i].text in event_name:
         continue
      event_name.append(tags_name[i].text.strip())
target_class_date_time = "title-date"
tags_date_time= soup.find_all("p",class_=target_class_date_time)
for i in range(len(tags_date_time)):
    if tags_date_time[i] in event_date_time:
        continue
    event_date_time.append(tags_date_time[i].text.strip())
dataframe_set=pd.DataFrame(list(zip(event_name,event_date_time)),columns=["Names","Date and Time"])
dataframe_set.to_csv("Hac7.csv")

