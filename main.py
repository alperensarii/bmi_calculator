from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("BMI Calculator")
window.config(padx=30,pady=30)

def calculate_bmi():
    height = entry_2.get()
    weight = entry_1.get()

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height")

    else:
        try:
            bmi =   float(weight) / (float(height) / 100)  ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Entry Valid Number")

        


label_1 = Label(text="Enter Your Weight (kg)",padx=20,pady=8)
label_1.pack()

entry_1 = Entry(width=8,bg="white",fg="black")
entry_1.pack()


label_2 = Label(text="Enter Your Height (cm)",padx=20,pady=8)
label_2.pack()

entry_2 = Entry(width=8, bg="white",fg="black")
entry_2.pack()

button = Button(text="Calculate", command=calculate_bmi)
button.pack()

result_label = Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Your BMI is {round(bmi,2)}. You are "

    if bmi <= 16:
        result_string += "severely thin"
    elif bmi > 16 and bmi <= 17:
        result_string += "moderately thin"
    elif bmi > 17 and bmi <= 18.5:
        result_string +=  "mild thin"
    elif bmi > 18.5 and bmi <= 25:
        result_string +=  "normal"
    elif bmi > 25 and bmi <= 30:
        result_string +=  "overweight"
    elif bmi > 30 and bmi <= 35:
        result_string +=  "obese class 1"
    elif bmi > 35 and bmi <= 40:
        result_string +=  "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string
window.mainloop()