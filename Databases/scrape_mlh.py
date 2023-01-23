from bs4 import BeautifulSoup
import requests
import pandas as pd

topic_url = "https://mlh.io/seasons/2023/events"

response = requests.get(topic_url)
restext = response.text

event_names = list()
event_dates = list()
event_months=list()
event_location = list()
event_hybrid_notes = list()
event_links = list()

soup = BeautifulSoup(restext, 'html5lib')

#######################################################################################
target_class = 'event-name'
tags_name = soup.find_all('h3', class_=target_class)
for i in range(len(tags_name)):
	event_names.append(tags_name[i].text)
#print("Total number of listed hackathons are {}: ".format(len(names)))
#for i in range(len(event_names)):
#	print(event_names[i])
########################################################################################

target_class_date = 'event-date'
tags_date = soup.find_all('p', class_ = target_class_date)
for i in range(len(tags_date)):
	event_dates.append(tags_date[i].text.strip())
event_months=[obb.split(" ")[0] for obb in event_dates]
#for i in range(len(event_dates)):
#	print(event_dates[i])

#########################################################################################


target_event_location = "event-location"
tags_location = soup.find_all('div', class_ = target_event_location)
for i in range(len(tags_location)):
	event_location.append(tags_location[i].text)


#########################################################################################
target_event_hybrid = "event-hybrid-notes"
tags_hybrid = soup.find_all('div', class_ = target_event_hybrid)
for i in range(len(tags_hybrid)):
	event_hybrid_notes.append(tags_hybrid[i].text.strip())
for i in range(len(event_hybrid_notes)):
    if event_hybrid_notes[i]=="Digital Only":
        event_hybrid_notes[i]="online"
    elif event_hybrid_notes[i]=="Hybrid, In-Person Focus":
        event_hybrid_notes[i]="hybrid"
    elif event_hybrid_notes[i]=="In-Person Only":
        event_hybrid_notes[i]="in_person"


#for i in range(len(event_hybrid_notes)):
#	print(event_hybrid_notes[i])

##########################################################################################

target_event_link = "event-link"
tags_links = soup.find_all('a', class_=target_event_link)
for i in range(len(tags_links)):
	event_links.append(tags_links[i]['href'])
##for i in range(len(event_links)):
##	print(event_links[i])


##########################################################################################

#dict = {"Event_Name":event_names, "Event_"}

dataframe_set = pd.DataFrame(list(zip(event_names, event_dates, event_months,event_location, event_hybrid_notes, event_links)), columns = ["Names", "Date", "Month","Location", "Notes", "Link"])
 
dataframe_set.to_csv('Hac10.csv')
