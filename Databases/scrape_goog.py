from bs4 import BeautifulSoup
import pandas as pd 
import requests 
event_name=list()
event_date_time=list()
link_lists=["https://gdg.community.dev/events/details/google-gdg-coimbatore-presents-flutter-forward-viewing-party/","https://gdg.community.dev/events/details/google-gdg-cloud-coimbatore-presents-cloud-open-house-2023-02-18/","https://gdg.community.dev/events/details/google-gdg-cloud-coimbatore-presents-cloud-open-house-2023-03-18/","https://gdg.community.dev/events/details/google-gdg-cloud-coimbatore-presents-cloud-open-house-2023-04-15/","https://gdg.community.dev/events/details/google-gdg-cloud-coimbatore-presents-cloud-open-house-2023-05-20/","https://gdg.community.dev/events/details/google-gdg-cloud-coimbatore-presents-cloud-open-house-2023-06-17/","https://gdg.community.dev/events/details/google-gdg-cloud-kochi-presents-ai-adapt-search-1st-edition/","https://gdg.community.dev/events/details/google-gdg-cloud-madurai-presents-cloud-2023/","https://gdg.community.dev/events/details/google-gdg-madurai-presents-devhackathon-with-flutter-2023/","https://gdg.community.dev/events/details/google-gdg-cloud-mumbai-presents-google-cloud-platform-in-2023/","https://gdg.community.dev/events/details/google-gdg-bhubaneswar-presents-product-development-lifecycle/","https://gdg.community.dev/events/details/google-gdg-ranchi-presents-flutter-forward-extended-ranchi/","https://gdg.community.dev/events/details/google-gdg-kolkata-presents-droidfest-kolkata-2023/","https://gdg.community.dev/events/details/google-gdg-sonargaon-presents-devfest-bangladesh-2022-gdg-sonargaon/","https://gdg.community.dev/events/details/google-gdg-sonargaon-presents-flutter-lab-02/","https://gdg.community.dev/events/details/google-gdg-ludhiana-presents-smart-hackathon-2023/","https://gdg.community.dev/events/details/google-gdg-islamabad-presents-women-techmakers-international-womens-day-conference/","https://gdg.community.dev/events/details/google-gdg-bangkok-presents-firebase-dev-day-2023/","https://gdg.community.dev/events/details/google-gdg-kabul-presents-devfest-kabul-afghanistan/","https://gdg.community.dev/events/details/google-gdg-dubai-presents-best-practices-improve-your-flutter-app/"]
for li in link_lists:
  response = requests.get(li)
  restext = response.text
  soup = BeautifulSoup(restext,"html5lib")
  target_class_name="font_banner2"
  tags_name=soup.find_all("span",class_=target_class_name)
  for i in range(len(tags_name)):
      if tags_name[i].text in event_name:
         continue
      event_name.append(tags_name[i].text)
  tags_class_date="event-date-time"
  tags_date=soup.find_all("div",class_=tags_class_date)
  for i in range(len(tags_date)):
      if tags_date[i].text in event_date_time:
         continue
      event_date_time.append(tags_date[i].text)
dataframe_set=pd.DataFrame(list(zip(event_name,event_date_time)),columns=["Names","Date and Time"])
dataframe_set.to_csv("Hac3.csv")
