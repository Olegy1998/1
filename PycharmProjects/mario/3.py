money = int(input("Введите число, с которого нужно выдать cдачу: "))
if money > 0 and money <= 99:
for i in range(money):
ch1 = money // 50
ch11 = money - 50 * ch1
ch2 = ch11 // 10
ch22 = ch11 - 10*ch2
ch3 = ch22 // 5
ch33 = ch22 - 5*ch3
ch4 = ch33 // 1
print(ch1,ch2,ch3,ch4)