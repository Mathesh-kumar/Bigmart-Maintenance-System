import pymongo
from bson.objectid import ObjectId
from datetime import date

def add_product(client, data):
    database = client['bigmart']
    customerCollection = database['products']
    customerCollection.insert_one(data)
    return True

def get_products(client):
    database = client['bigmart']
    customerCollection = database['products']
    products = list(customerCollection.find({}))
    category = [i['pCategory'] for i in products]
    productEach = []
    for i in set(category):
        categoryProducts = [j for j in products if j['pCategory'] == i]
        productEach.append([i, categoryProducts])
    return productEach

def view_product(client, prId):
    database = client['bigmart']
    customerCollection = database['products']
    product = list(customerCollection.find({"_id": ObjectId(prId)}))
    return product[0]

def delete_product(client, pName):
    database = client['bigmart']
    customerCollection = database['products']
    customerCollection.delete_one({"pName":pName})

def modify_product(client, data):
    database = client['bigmart']
    customerCollection = database['products']
    customerCollection.update_one({"pName":data['pName']}, {"$set":{
        "pStock":data['pStock'],
        "pPrice":data['pPrice'],
        "pPurchaseDate":data['pPurchaseDate'],
        "pExpiryDate":data['pExpiryDate']
    }}, upsert=False)

def notification(client):
    products = get_products(client)
    expiryDate = []
    lessProduct = []
    for i in range(len(products)):
        for j in products[i][1]:
            print(j)
            y,m,d = map(int, j['pExpiryDate'].split('-'))
            expDate = date(y,m,d)
            delta = expDate - date.today()
            if delta.days <= 3:
                expiryDate.append(j)
            if int(j['pStock']) < 10:
                lessProduct.append(j)
    notifyProducts = [expiryDate,lessProduct]
    return notifyProducts


def customers(client):
    database = client['bigmart']
    customerCollection = database['customers']
    customers = list(customerCollection.find({}))
    return customers

def view_customer(client, cId):
    database = client['bigmart']
    customerCollection = database['customers']
    customer = list(customerCollection.find({"_id": ObjectId(cId)}))
    return customer[0]

def purchase_product(client, prId):
    database = client['bigmart']
    customerCollection = database['products']
    product = list(customerCollection.find({"_id": ObjectId(prId)}))
    return product[0]

def add_sales_details(client, salesDetails):
    database = client['bigmart']
    salesCollection = database['salesdetails']
    salesCollection.insert_one(salesDetails)

def product_purchase(client, pName, pCount):
    database = client['bigmart']
    customerCollection = database['products']
    product = list(customerCollection.find({"pName": pName}))
    product =  product[0]
    if int(product['pStock']) < int(pCount):
        return False
    else:
        newStock = int(product['pStock']) - int(pCount)
        customerCollection.update_one({"pName":pName}, {"$set":{
        "pStock":str(newStock)
    }}, upsert=False)

        delta = date.today()
        todayDate = delta.strftime("%Y-%m-%d")
        sPrice = int(pCount)*int(product['pPrice'])
        salesDetails = dict(pId=product['_id'], sDate=todayDate, sQuantity=pCount, sPrice=str(sPrice))
        add_sales_details(client, salesDetails)
        return True

def dashboard_results(client):
    dbResults = {}
    database = client['bigmart']

    salesDetails = database['salesdetails']
    sales = list(salesDetails.find({}))
    totalSales = 0
    for i in sales:
        totalSales = totalSales + int(i['sPrice'])
    dbResults['totalSales'] = str(totalSales)

    customerDetails = database['customers']
    customers = list(customerDetails.find({}))
    dbResults['totalCustomers'] = str(len(customers))

    return dbResults

def analytics_result(client):
    database = client['bigmart']
    productsCollection = database['products']
    products = list(productsCollection.find({}))
    chartOne = [[], []]
    for i in products:
        chartOne[0].append(i['pName'])
        chartOne[1].append(i['pStock'])
    print(chartOne)
    return chartOne
