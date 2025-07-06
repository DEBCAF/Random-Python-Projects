def sumpalin(num):
    list = []
    while num > 0:
        temp = largestpalin(num)
        list.append(temp)
        num -= temp
    return list
    
def largestpalin(num):
    while not(ispalin(num)):
        num -= 1
    return num
    
def ispalin(num):
    num = str(num)
    palin = False
    for i in range(len(num)//2):
        if num[i] == num[len(num)-i-1]:
            palin = True
        else:
            palin = False
            break
    if len(num) == 1:
        palin = True
    return palin

user = int(input("Enter a number: "))
print(sumpalin(user))