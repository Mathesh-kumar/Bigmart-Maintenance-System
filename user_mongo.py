import pymongo

def find_existing_user(customerCollection, cMailId):
    userExist = customerCollection.find({"cMailId":cMailId})
    for i in enumerate(userExist):
        return True
    return False

def user_registration(client, data):
    database = client['bigmart']
    customerCollection = database['customers']
    if find_existing_user(customerCollection, data['cMailId']):
        return False
    else:
        customerCollection.insert_one(data)
        return True

def user_login(client, data):   
    database = client['bigmart']
    customerCollection = database['customers']
    if find_existing_user(customerCollection, data['cMailId']):
        userExist = customerCollection.find({"cMailId":data['cMailId']})
        print(userExist[0]['cMailId'], userExist[0]['cPassword'], userExist[0]['cIsAdmin'])
        if userExist[0]['cPassword'] == data['cPassword'] and userExist[0]['cIsAdmin'] == "True":
            return (True, True)
        elif userExist[0]['cPassword'] == data['cPassword'] and userExist[0]['cIsAdmin'] == "False":
            return (True, False)
        return (False, False)
    return (False, False)