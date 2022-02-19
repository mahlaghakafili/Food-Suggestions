  function BMIcalculator() {
        // user inputs
        var heightcm = Number(document.getElementById("height").value);
        var weight = Number(document.getElementById("weight").value);
        //convert cm to meter
        var heightmeter=heightcm/100
        var BMI = Math.round(weight / (heightmeter**2));
        //Display result of calculation
        document.getElementById("output").innerText ='ur BMI is'+" "+BMI

        var output = Math.round(BMI * 100) / 100;
        if (output < 18.5)
          document.getElementById("result").innerText = "Underweight,wOoh! you are Underweight u can join us";
        else if (output >= 18.5 && output <= 25)
          document.getElementById("result").innerText = "Normal,wOoh! you are Normal u can join us";
        else if (output >= 25 && output <= 30)
          document.getElementById("result").innerText = "Obese,wOoh! you are Obese u can join us";
        else if (output > 30)
          document.getElementById("result").innerText = "Overweight,oh! sorry you are overweight u can't join us";
}