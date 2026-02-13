test = [100,90,80,70,60]
count = 0
score = 0
aberage = 0
while int(count) < int(len(test)):
    score = score + test[count]
    aberage = score / len(test)
    count = count + 1
print(f"合計値：{score}")
print(f"平均値：{aberage}")
