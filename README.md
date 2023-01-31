# Hack-API

<img width="1428" alt="94BDBB78-F5E1-4169-AADF-FB40303DA0F1" src="https://user-images.githubusercontent.com/97288756/215721503-36096b60-5b29-42ce-9b1d-7de821b94f9c.png">


Hack-Api is an API which provides data and details about most of the technical events including Hackathons , GDG-Events , AWS- Events , Microsoft Azure Events , iOS events , Student Developer Details.  
# Tech Stacks Used
- FastAPI
- MongoDB
- Jinja 2.0 
- JWT 
- RS256
- DockerFile

# Installation 

1. Using Docker (Must have Docker Desktop installed and it must be running )

```
docker pull achiverram28/hack-api-image:latest
docker run -d --name <yourcontainername> -p 80:80 achiverram28/hack-api-image:latest

```
2. Using Git Clone
```
// Install your virtual environment and switch it on 

// Cloning the Repository
git clone https://github.com/achiverram28/Hack-API.git

// Installing the dependencies
pip3 install -r requirements.txt

//Running the server
uvicorn app.main:app --reload

```
## Swagger UI Docs

<img width="1405" alt="Image" src="https://user-images.githubusercontent.com/97288756/215673473-7dc38c90-8380-4357-8ac2-aeab209cd0e6.jpeg">

<img width="1405" alt="3E7D2E67-71EE-4D1A-98FB-A8521538E90A" src="https://user-images.githubusercontent.com/97288756/215673485-3b932c04-aef3-4e65-8961-7706baa0dcfc.png">

<img width="1405" alt="4156AAD3-C12A-4839-B8A7-18F142E4A3D7" src="https://user-images.githubusercontent.com/97288756/215673752-35262be8-2c6d-4ca9-9f40-6e6e7421cda8.png">

<img width="1405" alt="0BA3D0C7-E7B0-49CD-BEF8-542CCD9FB8C4" src="https://user-images.githubusercontent.com/97288756/215673789-0e296f96-aa0d-47fc-bf80-e4f32bb8fc4b.png">


## Naming Guidelines

- When you want to enter the month name in the url , enter the first three letters of the month name with first letter being captial and the rest being in lower case : Ex January => Jan . ** Only in Open Source events use full name of month :Ex January => January. **

- For type of event in mlh you will have to use => a) online b) in_person c) hybrid

- For name , if you have spaces in the event name, cover it up with _   . Example : Google Summer of Code => Google_Summer_of_Code

## Guidelines and Usage 

- Before using the API , you will have to register for the first time . That has to be done using the http:127.0.0.1/docs , here go to /api/auth/register and click on Try It and then Execute

![11E8746B-0440-411C-BAC8-E25443A54DCF_1_105_c](https://user-images.githubusercontent.com/97288756/215720421-108edd72-8653-4487-8a35-2bb76139f08c.jpeg)


- From the next time , you will have to login before you will start using it . That has to be done using the http:127.0.0.1/docs , here go to /api/auth/login and click on Try It and then Execute.

![2A0DA070-EB6C-46AB-B5B6-E9D409A1FF7E_1_105_c](https://user-images.githubusercontent.com/97288756/215720456-d0ff17d1-9801-4b36-b631-c4b3e37144fd.jpeg)

- If you want to logout , then you will have to go to http:127.0.0.1/docs and /api/auth/logout and click on Try It and then Execute.

<img width="1408" alt="8D7EB593-E95E-4DC7-9786-D065FB3DEC35" src="https://user-images.githubusercontent.com/97288756/215720507-0dfdc4f8-86e4-4215-90ea-37a5fc5b5647.png">

## Usage Modes

- Normal Web Version => Data in formatted web page

- Api Developer Version => Data in json format , where the developers can use the json format for indexing and using the data . If you add .json at the end of the url , you will be able to see this. 

## Features 

- Hackathons => { MLH, DEVFOLIO , OPEN SOURCE , COMPETITIVE CODING }

-  GDG EVENTS 

- AWS EVENTS 

- MICROSOFT AZURE EVENTS 

- STUDENT DEVELOPER SUPPORT DETAILS

## Developer 

Ram Samarth B B => achiverram28@gmail.com  
