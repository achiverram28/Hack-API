# Hack-API

![B27E67BB-CC0C-4C05-905F-90CA19261817_4_5005_c](https://user-images.githubusercontent.com/97288756/215660731-c8413435-6714-43c2-933a-16977ba2a74c.jpeg)

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


## Usage and Naming Guidelines

- When you want to enter the month name in the url , enter the first three letters of the month name with first letter being captial and the rest being in lower case : Ex January => Jan . ** Only in Open Source events use full name of month :Ex January => January. **

- For type of event in mlh you will have to use => a) online b) in_person c) Hybrid

- For name , if you have spaces in the event name, cover it up with _   . Example : Google Summer of Code => Google_Summer_of_Code


