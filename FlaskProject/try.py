from flask import Flask, render_template
from flask import request, redirect, session, url_for
from datetime import timedelta
import cgi
app = Flask(__name__)
app.secret_key='mahli'
app.permanent_session_lifetime=timedelta(minutes=5)
userpass = {'mahli': '0987', 'mahjabin': '9876', 'einali': '1360', 'mahlagha': '1234'}


@app.route("/",methods=['POST','GET'])
def homepage():
    session.permanent = True
    return render_template("homepage.html")


@app.route("/signin/",methods=['POST','GET'])
def signin():
    session.permanent=True
    return render_template('signin.html')



@app.route('/bmi/',methods=['POST','GET'])
def bmi():
    session.permanent = True
    if request.method== "POST":
        if request.form['user'] in userpass and request.form['pass'] in userpass.values():
            return redirect(url_for('bmi'))
        else:
            return render_template("notuser.html")
    else:
        return render_template('bmi.html')


@app.route('/result', methods=['POST',"GET"])
def result():
    session.permanent = True
    if request.method == "POST":
        height = request.form['height']
        weight = request.form['weight']
        session['height']=height
        session['weight']=weight
        BMI = (int(session['weight']) / ((int(session['height'])/100)**2))
        bmi = round(BMI * 100) / 100
        session["bmi"]=bmi
        if bmi < 18.5:
            massage = "Underweight,wOoh! you are Underweight u can join us"
            t = 0
        elif bmi >= 18.5 and bmi <= 25:
            massage = "Normal,wOoh! you are Normal u can join us"
            t = 0
        elif bmi >= 25 and bmi <= 30:

            massage = "Obese,wOoh! you are Obese u can join us"
            t = 0
        elif bmi > 30:
            massage = "Overweight,oh! sorry you are overweight u can't join us"
            t = 1
        session['massage']=massage
        if t == 1:
            return render_template("badresult.html", bmi1=bmi)
        else:
            return render_template("result.html", bmi1=bmi, massage1=massage)
    else:
        bmi=session["bmi"]
        massage=session['massage']
        return render_template("result.html",bmi1=bmi, massage1=massage)


@app.route('/info/', methods=['POST','Get'])
def info():
    session.permanent = True
    return render_template("info.html")



@app.route('/contact/', methods=['POST','Get'])
def contact():
    session.permanent = True
    if request.method == "POST":
        name=request.form['name']
        session['name']=name
        firstname=request.form['fname']
        session['fname']=firstname
        return redirect(url_for('contact'))
    else:
        return render_template("contact.html")

@app.route('/lifestyle/', methods=['POST',"GET"])
def lifestyle():
    session.permanent = True
    if request.method == "POST":
        email=request.form['email']
        session['email'] =email
        phone=request.form['phone']
        session['phone'] =phone
        return redirect(url_for('lifestyle'))
    else:
        return render_template("lifestyle.html")

@app.route('/suggestion/', methods=['POST',"GET"])
def suggestion():
    session.permanent = True

    def namefname():
        namee=session['name']
        fnamee=session['fname']
        return namee.upper()+" "+fnamee.upper()

    lifestyles=request.form["lifestylediet"]
    session['lifestyles']=lifestyles
    life = session['lifestyles']
    if life == "veg":
        food = "Vegetable Soup"
    else:
        food = "Butter Chicken"
    def contactname():
        email=session['email']
        phone=session['phone']
        return f"we have your email: {email} and your phone: {phone}"
    return render_template("suggestion.html", food1=food,name=namefname(),contact=contactname())

@app.route('/logout/')
def logout():
    session.clear()
    return render_template('logout.html')
if __name__ == "__main__":
    app.run(debug=True)
