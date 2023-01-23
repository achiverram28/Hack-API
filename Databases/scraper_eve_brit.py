from bs4 import BeautifulSoup
import requests
import pandas as pd 
event_names=list()
event_date=list()
for i in range(1,501):
    topic_url="https://www.eventbrite.com/d/online/hackathon/?page={}".format(i)
    response = requests.get(topic_url)
    restext=response.text
    soup=BeautifulSoup(restext,"html5lib")
####################################
    target_class_name='eds-event-card__formatted-name--is-clamped'
    tags_name=soup.find_all('div',class_=target_class_name)
    for i in range(len(tags_name)):
      if tags_name[i].text in event_names:
         continue
      event_names.append(tags_name[i].text)
    target_class_subtitle='eds-event-card-content__sub-title'
    tags_subtitle=soup.find_all('div',class_=target_class_subtitle)
    for i in range(len(tags_subtitle)):
        if tags_subtitle[i].text in event_date:
            event_date.append(tags_subtitle[i].text)
        event_date.append(tags_subtitle[i].text)
dataframe_set = pd.DataFrame(list(zip(event_names,event_date)),columns=["Names","Date and Time"])
dataframe_set.to_csv("Hac3.csv")
