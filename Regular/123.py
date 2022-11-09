num = True
numsum = 0
while num != 0:
    num  = int(input("Введите чило"))
    if num % 6 == 0 and num % 10 == 4:
        numsum += num
print(numsum)