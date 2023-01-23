from bs4 import BeautifulSoup
import requests
import pandas as pd 
event_names=list()
event_dates=list()
link_lists=["https://hackshetra-23.devfolio.co/","https://octahacks.devfolio.co/","https://bitnbuild.netlify.app/","https://ingenious-hackathon-4.devfolio.co/","https://lnmhacks.devfolio.co/","https://castor-2023.devfolio.co/","https://unscript2k23.devfolio.co/","https://ethforall.devfolio.co/","https://hackoverflow2.devfolio.co/","https://dotslash-6.devfolio.co/","https://sbssu-smart-hackathon.devfolio.co/","https://hack-infinity.devfolio.co/","https://unscript-rookies-hackathon-k.devfolio.co/","https://technex-hackathon-2.devfolio.co/","https://hack-jmi.devfolio.co/","https://vashist.devfolio.co/","https://reckon-4.devfolio.co/","https://hackbrewer.devfolio.co/","https://diversion2k23.devfolio.co/","https://duhacks2.devfolio.co/","https://hackmol-2.devfolio.co/","https://ur-hackathon-2.devfolio.co/","https://innerve-seven.devfolio.co/","https://nebula.devfolio.co/","https://cybershadez-23.devfolio.co/","https://hult-prize-bvcoe-1.devfolio.co/","https://hackbeats.devfolio.co/","https://nawabathon.devfolio.co/","https://edu-hack.devfolio.co/","https://edu-hack.devfolio.co/","https://nmithacks.devfolio.co/"]
for li in link_lists:
  topic_url = li
  response = requests.get(topic_url)
# restext = response.text
# print(response.status_code)
  soup = BeautifulSoup(response.content,"html5lib")
################################################
  target_class_name="cdNzRb"
  tags_name=soup.find_all("h1",class_=target_class_name)
# print(tags_name)
  for i in range(len(tags_name)):
       if tags_name[i].text in event_names:
         continue
       event_names.append(tags_name[i].text)
# print(event_names)
################################################
  target_class_date="hbClIC"
  tags_date=soup.find_all("p",class_=target_class_date)
# print(tags_name)
  for i in range(len(tags_date)):
       if tags_date[i].text in event_dates:
         continue
       event_dates.append(tags_date[i].text)
# print(event_dates)
################################################
dataframe_set = pd.DataFrame(list(zip(event_names,event_dates)),columns=["Names","Date and Time"])
dataframe_set.to_csv("Hac4.csv")
