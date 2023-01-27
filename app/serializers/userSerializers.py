def userEntity(user):
    return {
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "photo":user["photo"],
        "verified":user["verified"],
        "password":user["password"],
        "created_at":user["created_at"],
        "updated_at":user["updated_at"]
    }
def userResponseEntity(user):
    return {
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "photo":user["photo"],
        "created_at":user["created_at"],
        "updated_at":user["updated_at"]
    }
def embeddedUserResponse(user):
    return {
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "photo":user["photo"]
    }
def userListEntity(users):
    return [userEntity(user) for user in users]
    
