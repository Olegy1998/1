x=int(input("Введите высоту : "))
if x > 0 and x < 23:
for i in range(x):
print(' ' * (x-i-1) + '*' * (i+2))