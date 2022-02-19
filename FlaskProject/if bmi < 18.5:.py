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


    height = request.form['height']
    weight = request.form['weight']
    bmi = round(weight / (height**2))        




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
    if t == 1:
        return render_template("badresult.html", bmi1=bmi)
    else:


        if bmi <= 25:
        if life == "veg":
            food = "mahli1"
        else:
            food = "mahli2"
    else:
        if life == "nonveg":
            food = "mahli2"
        else:
            food = "mahli3"


height = request.form['height']
    weight = request.form['weight']
    BMI = (int(weight) / ((int(height)/100)**2))
    bmi = round(BMI * 100) / 100
    life = request.form["lifestylediet"]
    if bmi <= 25:
        if life == "veg":
            food = "mahli1"
        else:
            food = "mahli2"
    else:
        if life == "nonveg":
            food = "mahli2"
        else:
            food = "mahli3"            