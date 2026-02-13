height = float(input("身長を入力してください"))
weight = float(input("体重を入力してください"))
bmi = weight / (height*height)
print("BMI:" + str(bmi))  #strに変換しないとエラー吐く
print(f"BMI:{bmi}") #こっちの方がスマート
print(f"BMI:{bmi:.2f}") #小数点の表示制限（数字自体は変わってない）
bmi = round(bmi , 2) #四捨五入はround
print("BMI:" + str(bmi))