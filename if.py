height = float(1.7)
weight = int(60)
bmi = weight / (height*height)
print(bmi)
if(bmi < 18.5):
    print("痩せ")
elif(bmi >= 18.5 and bmi < 25):
    print("普通")
else:
    print("肥満")