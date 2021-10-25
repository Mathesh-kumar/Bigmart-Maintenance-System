from flask import Flask, render_template, request, jsonify, redirect
# from flask.helpers import urlfor
import pymongo
import user_mongo
import admin_mongo
import os
import json

app = Flask(__name__)

"""
mongodb+srv://bigmart:bigmart@bigmart-cluster.bgwec.mongodb.net/BigMart?retryWrites=true&w=majority
"""

def open_credential():
    client = pymongo.MongoClient(f"mongodb://localhost:27017/")
    return client

def close_credential(client):
    client.close()

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

@app.route('/<pagename>', methods=['GET'])
def admin_pages(pagename):
    if pagename == "dashboard":
        dbResults = admin_mongo.dashboard_results(client)
        return render_template('dashboard.html', dbResults=dbResults)
    elif pagename == "notification":
        notify = admin_mongo.notification(client)
        return render_template('notification.html', notify=notify)
    elif pagename == "products":
        product_each = admin_mongo.get_products(client)
        return render_template('products.html', product_each=product_each)
    elif pagename == "customers":
        customers = admin_mongo.customers(client)
        return render_template('customers.html', customers=customers)
    elif pagename == "analytics":
        analyticsResult = admin_mongo.analytics_result(client)
        return render_template('analytics.html', analyticsResult=json.dumps(analyticsResult))

@app.route('/user/<pagename>', methods=['GET'])
def user_pages(pagename):
    if pagename == "userproducts":
        product_each = admin_mongo.get_products(client)
        return render_template('userproducts.html', product_each=product_each)

@app.route('/register', methods=['POST'])
def register():
    cMailId = request.form['mail']
    cName = request.form['uname']
    cPassword = request.form['psw']
    cContactNo = request.form['mobileno']
    cAddress = request.form['address']
    
    cImage = request.files['image']
    path = os.path.join(r'C:\Users\Abilash\Desktop\SDL\Bigmart-Maintenance-System\static\images', cImage.filename)
    cImage.save(path)
    
    userData = dict(cMailId=cMailId, cName=cName, cPassword=cPassword, cContactNo=cContactNo, cAddress=cAddress, cImage=cImage.filename, cIsAdmin="False")
    
    try:
        userRegister = user_mongo.user_registration(client, userData)
        if userRegister:
            return render_template('index.html', register_success_modal=True, register_failure_modal=False)
        else:
            return render_template('index.html', register_success_modal=False, register_failure_modal=True)
    except:
        return jsonify(dict(replyCode=0, replyMessage="Error in new user registration"))


@app.route('/login', methods=['POST'])
def login():
    cMailId = request.form['mail']
    cPassword = request.form['psw']
    userData = dict(cMailId=cMailId, cPassword=cPassword)
    
    try:
        userLogin, isAdmin = user_mongo.user_login(client,userData)
        print(userLogin, isAdmin)
        if userLogin and isAdmin:
            dbResults = admin_mongo.dashboard_results(client)
            return render_template('dashboard.html', dbResults=dbResults)
        elif userLogin:
            product_each = admin_mongo.get_products(client)
            return render_template('userproducts.html', product_each=product_each)
        else:
            return render_template('index.html', login_failure_modal=True)
    except:
        return jsonify(dict(replyCode=0, replyMessage="Error in user login"))

@app.route('/addproduct', methods=['POST'])
def add_product():
    pName = request.form['pname']
    pCategory = request.form['pcategory']
    pStock = request.form['pstock']
    pPrice = request.form['pprice']
    pDescription = request.form['pdescription']
    pImage = request.files['pimage']
    pPurchaseDate = request.form['ppurchasedate']
    pExpiryDate = request.form['pexpirydate']

    addProductData = dict(pName=pName, pCategory=pCategory, pStock=pStock, pPrice=pPrice, pDescription=pDescription, pImage=pImage.filename, pPurchaseDate=pPurchaseDate, pExpiryDate=pExpiryDate)
    path = os.path.join(r'C:\Users\Abilash\Desktop\SDL\Bigmart-Maintenance-System\static\images', pImage.filename)
    pImage.save(path)

    try:
        addProduct = admin_mongo.add_product(client, addProductData)
        product_each = admin_mongo.get_products(client)
        return render_template('products.html', product_each=product_each)
    except:
        return jsonify(dict(replyCode=0, replyMessage="Error in add new product"))

@app.route('/viewproducts/<prId>', methods=['GET'])
def view_product(prId):
    productDetails = admin_mongo.view_product(client, prId)
    return render_template('viewproducts.html', productDetails=productDetails)

@app.route('/modifyproduct', methods=['POST'])
def modify_product():
    pName = request.form['pname']
    pStock = request.form['pstock']
    pPrice = request.form['pprice']
    pPurchaseDate = request.form['ppurchasedate']
    pExpiryDate = request.form['pexpirydate']

    modifyProductData = dict(pName=pName, pStock=pStock, pPrice=pPrice, pPurchaseDate=pPurchaseDate, pExpiryDate=pExpiryDate)

    try:
        modifyProduct = admin_mongo.modify_product(client, modifyProductData)
        product_each = admin_mongo.get_products(client)
        return render_template('products.html', product_each=product_each)
    except:
        return jsonify(dict(replyCode=0, replyMessage="Error in add new product"))

@app.route('/delete/<pName>', methods=['GET'])
def delete_product(pName):
    admin_mongo.delete_product(client, pName)
    product_each = admin_mongo.get_products(client)
    return render_template('products.html', product_each=product_each)

@app.route('/notification', methods=['GET'])
def notification():
    notify = admin_mongo.notification(client)
    return render_template('notification.html', notify=notify)

@app.route('/customers', methods=['GET'])
def customers():
    customers = admin_mongo.customers(client)
    return render_template('customers.html', customers=customers)

@app.route('/viewcustomers/<cId>', methods=['GET'])
def view_customer(cId):
    customerDetails = admin_mongo.view_customer(client, cId)
    return render_template('viewcustomers.html', customerDetails=customerDetails)

@app.route('/purchaseproducts/<pId>', methods=['GET'])
def purchase_product(pId):
    productDetails = admin_mongo.purchase_product(client, pId)
    return render_template('purchaseproducts.html', productDetails=productDetails, purchaseDetails="1")

@app.route('/purchaseproduct/<pName>', methods=['POST'])
def product_purchase(pName):
    pCount = request.form['count']
    purchaseDetails = admin_mongo.product_purchase(client, pName, pCount)
    return render_template('purchaseproducts.html', purchaseDetails=purchaseDetails, productDetails="1")

@app.route('/analytics', methods=['GET'])
def analytics():
    analyticsResult = admin_mongo.analytics_result(client)
    return render_template('analytics.html', analyticsResult=json.dumps(analyticsResult))


if __name__ == '__main__':
    client = open_credential()
    app.run(debug=True)
    close_credential(client)