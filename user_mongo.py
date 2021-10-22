import pymongo

def find_existing_user(customerCollection, uname):
    userExist = customerCollection.find({"uname":uname})
    for i in enumerate(userExist):
        print("1",i)
        return True
    return False

def user_registration(client, data):
    database = client['BigMart']
    customerCollection = database['customer']
    if find_existing_user(customerCollection, data['uname']):
        return False
    else:
        customerCollection.insert_one(data)
        return True

def user_login(client, data):
    database = client['BigMart']
    customerCollection = database['customer']
    if find_existing_user(customerCollection, data['uname']):
        userExist = customerCollection.find({"uname":data['uname']})
        if userExist[0]['pwd'] == data['pwd']:
            return True
        return False
    return False