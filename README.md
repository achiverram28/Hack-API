# Hack-API

![B27E67BB-CC0C-4C05-905F-90CA19261817_4_5005_c](https://user-images.githubusercontent.com/97288756/215660731-c8413435-6714-43c2-933a-16977ba2a74c.jpeg)

Hack-Api is an API which provides data and details about most of the technical events including Hackathons , GDG-Events , AWS- Events , Microsoft Azure Events , iOS events , Student Developer Details.  
# Tech Stacks Used
- Fast API
- MongoDB
- Jinja 2.0 
- JWT 
- Bcrypt
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

