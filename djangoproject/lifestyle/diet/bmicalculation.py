class BmiCalculation:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi_calculation(self):
        Bmi = (int(self.weight) / ((int(self.height) / 100) ** 2))
        bmi_number = round(Bmi * 100) / 100
        return bmi_number

    def bmi_massage(self):

        global bmi_massage
        if self.bmi_calculation() < 18.5:
            bmi_massage = "Underweight,wOoh! you are Underweight u can join us"
        elif 18.5 <= self.bmi_calculation() <= 25:
            bmi_massage = "Normal,wOoh! you are Normal u can join us"
        elif 25 <= self.bmi_calculation() <= 30:
            bmi_massage = "Obese,wOoh! you are Obese u can join us"
        elif self.bmi_calculation() > 30:
            bmi_massage = "Overweight,oh! sorry you are overweight u can't join us"
        return bmi_massage

    def entrance_validation(self):
        global entrance_validation

        if self.bmi_calculation() > 30:
            entrance_validation = 1
        else:
            entrance_validation = 0
        return entrance_validation
