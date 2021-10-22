from flask import Flask, render_template, request, jsonify, redirect
# from flask.helpers import urlfor
import pymongo
import user_mongo

app = Flask(__name__)

def open_credential():
    client = pymongo.MongoClient(f"mongodb+srv://bigmart:bigmart@bigmart-cluster.bgwec.mongodb.net/BigMart?retryWrites=true&w=majority")
    return client

def close_credential(client):
    client.close()

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html')

@app.route('/notificationpage', methods=['GET'])
def notification_page():
    return render_template('notificationpage.html')

@app.route('/register', methods=['POST'])
def register():
        mail = request.form['mail']
        uname = request.form['uname']
        pwd = request.form['psw']
        userData = dict(mail=mail, uname=uname, pwd=pwd)
        
        try:
            userRegister = user_mongo.user_registration(client, userData)
            if userRegister:
                return render_template('landingpage.html', register_success_modal=True, register_failure_modal=False)
            else:
                return render_template('landingpage.html', register_success_modal=False, register_failure_modal=True)
        except:
            return jsonify(dict(replyCode=0, replyMessage="Error in new user registration"))


@app.route('/login', methods=['POST'])
def login():
        uname = request.form['uname']
        pwd = request.form['psw']
        userData = dict(uname=uname, pwd=pwd)
        
        try:
            userLogin = user_mongo.user_login(client,userData)
            if userLogin:
                return render_template('index.html')
            else:
                return render_template('landingpage.html', login_failure_modal=True)
        except:
            return jsonify(dict(replyCode=0, replyMessage="Error in user login"))



if __name__ == '__main__':
    client = open_credential()
    app.run(debug=True)
    close_credential(client)