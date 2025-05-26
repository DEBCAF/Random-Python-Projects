# Andrew Wong British Informatics Olympiad 2025 Question 1(a)
# Subroutines
def two(num):
    num = int(num)
    if (num%10)>(num//10):
        temp = (num//10)*10+(num//10)
        final = str(temp) + " " + str(num-temp)
        return final
    elif (num%10)<(num//10):
        temp = ((num//10)-1)*10+((num//10)-1)
        if temp == 0:
            return("9 1")
        elif (num-temp) == 10:
            final = str(temp) + " 9 1"
            return final
        else:
            final = str(temp) + " " + str(num-temp)
            return final
    else:
        return str(num)
def three(num):
    num = str(num)
    if int(num[2])>int(num[0]):
        temp = num[0]+num[1]+num[0]
        diff = str(int(num)-int(temp))
        if int(diff) < 10:
            final = temp + " " + diff
            return final            
        else:
            return (temp + " 9 1")
    elif int(num[2])<int(num[0]):
        if num[0] == "1":
            temp = "99"
        else:
            temp = str(int(num[0])-1)+"9"+str(int(num[0])-1)
        diff = str(int(num)-int(temp))
        if diff !="0":
            if len(diff) == 2:
                final = temp + " " + two(diff)
                return final
            elif len(diff) == 1:
                final = temp + " " + diff
                return final
            elif len(diff) == 3:
                final = temp + " " + three(diff)
                return final 
        else:
            return temp
    else:
        return str(num)

def four(num):
    num = str(num)
    if int(num[3])>=int(num[0]):
        if int(num[1])<int(num[2]):
            temp = num[0]+num[1]+num[1]+num[0]
            diff = str(int(num)-int(temp))
            if int(diff) > 9:
                final = temp + " " + two(diff)
                return final
            else:
                final = temp + diff
                return final
        elif int(num[1])>int(num[2]):
            temp = num[0]+str(int(num[1])-1)+str(int(num[1])-1)+num[0]
            diff = str(int(num)-int(temp))
            if diff !="0":
                if len(diff) == 3:
                    final = temp + " " + three(diff)
                    return final
                elif len(diff) == 2:
                    final = temp + " " + two(diff)
                    return final
                elif len(diff) == 1:
                    final = temp + diff
                    return final
            else: 
                return temp
        else:
            temp = num[0]+num[1]+num[1]+num[0]
            diff = str(int(num)-int(temp))
            final = temp + " " + diff
            return final
    elif int(num[3])<int(num[0]):
        if num[0] == "1":
            temp = "999"
        else:
            temp = str(int(num[0])-1)+"99"+str(int(num[0])-1)
        diff = str(int(num)-int(temp))
        if diff !="0":
            if len(diff) == 3:
                final = temp + " " + three(diff)
                return final
            elif len(diff) == 2:
                final = temp + " " + two(diff)
                return final
            elif len(diff) == 1:
                final = temp + diff
                return final
            elif len(diff) == 4:
                final = temp + " " + four(diff)
                return final
        else: 
            return temp
        
def five(num):
    num = str(num)
    if int(num[4])>=int(num[0]):
        if int(num[1])<=int(num[3]):
            if int(num[1])<int(num[2]):
                temp = num[0]+num[1]+num[2]+num[1]+num[0]
                diff = str(int(num)-int(temp))
                if diff != "0":
                    if len(diff) == 2:
                        final = temp +" "+two(diff)
                        return final
                    elif len(diff) == 1:
                        final = temp +" "+ diff
                        return final
                    elif len(diff) == 3:
                        final = temp+" "+three(diff)
                        return final
                    elif len(diff) == 4:
                        final = temp+" "+four(diff)
                        return final
                else: 
                    return temp
            elif int(num[1])>int(num[2]):
                temp = num[0]+str(int(num[1])-1)+"9"+str(int(num[1])-1)+num[0]
                diff = str(int(num)-int(temp))
                if diff != "0":
                    if len(diff) == 2:
                        final = temp +" "+two(diff)
                        return final
                    elif len(diff) == 1:
                        final = temp +" "+ diff
                        return final
                    elif len(diff) == 3:
                        final = temp+" "+three(diff)
                        return final
                    elif len(diff) == 4:
                        final = temp+" "+four(diff)
                        return final
                else: 
                    return temp
            else:
                temp = num[0]+num[1]+num[1]+num[1]+num[0]
                diff = str(int(num)-int(temp))
                if diff != "0":
                    if len(diff) == 2:
                        final = temp +" "+two(diff)
                        return final
                    elif len(diff) == 1:
                        final = temp +" "+ diff
                        return final
                    elif len(diff) == 3:
                        final = temp+" "+three(diff)
                        return final
                    elif len(diff) == 4:
                        final = temp+" "+four(diff)
                        return final
                else: 
                    return temp
        elif int(num[1])>int(num[3]):
            temp = num[0]+str(int(num[1])-1)+"9"+str(int(num[1])-1)+num[0]
            diff = str(int(num)-int(temp))
            if diff != "0":
                if len(diff) == 2:
                    final = temp +" "+two(diff)
                    return final
                elif len(diff) == 1:
                    final = temp +" "+ diff
                    return final
                elif len(diff) == 3:
                    final = temp+" "+three(diff)
                    return final
                elif len(diff) == 4:
                    final = temp+" "+four(diff)
                    return final
            else: 
                return temp
    elif int(num[4])<int(num[0]):
        if num[0] == "1":
            temp = "9999"
        else:
            temp = str(int(num[0])-1)+"999"+str(int(num[0])-1)
        diff = str(int(num)-int(temp))
        if diff != "0":
            if len(diff) == 2:
                final = temp +" "+two(diff)
                return final
            elif len(diff) == 1:
                final = temp +" "+ diff
                return final
            elif len(diff) == 3:
                final = temp+" "+three(diff)
                return final
            elif len(diff) == 4:
                final = temp+" "+four(diff)
                return final
            elif len(diff) == 5:
                final = temp+" "+five(diff)
                return final 
        else: 
            return temp
    
def six(num):
    num = str(num)
    if int(num[5])>=int(num[0]):
        if int(num[1])<=int(num[4]):
            if int(num[2])<=int(num[3]):
                temp = num[0]+num[1]+num[2]+num[2]+num[1]+num[0]
                diff = str(int(num)-int(temp))
                if diff != "0":
                    if len(diff) == 2:
                        final = temp +" "+two(diff)
                        return final
                    elif len(diff) == 1:
                        final = temp +" "+ diff
                        return final
                    elif len(diff) == 3:
                        final = temp+" "+three(diff)
                        return final
                    elif len(diff) == 4:
                        final = temp+" "+four(diff)
                        return final
                    elif len(diff) == 5:
                        final = temp+" "+five(diff)
                        return final
                else: 
                    return temp
            elif int(num[2])>int(num[3]):
                temp = num[0]+num[1]+str(int(num[2])-1)+str(int(num[2])-1)+num[1]+num[0]
                diff = str(int(num)-int(temp))
                if diff != "0":
                    if len(diff) == 2:
                        final = temp +" "+two(diff)
                        return final
                    elif len(diff) == 1:
                        final = temp +" "+ diff
                        return final
                    elif len(diff) == 3:
                        final = temp+" "+three(diff)
                        return final
                    elif len(diff) == 4:
                        final = temp+" "+four(diff)
                        return final
                    elif len(diff) == 5:
                        final = temp+" "+five(diff)
                        return final
                else: 
                    return temp
        elif int(num[1])>int(num[4]):
            temp = num[0]+num[4]+"99"+num[4]+num[0]
            diff = str(int(num)-int(temp))
            if diff != "0":
                if len(diff) == 2:
                    final = temp +" "+two(diff)
                    return final
                elif len(diff) == 1:
                    final = temp +" "+ diff
                    return final
                elif len(diff) == 3:
                    final = temp+" "+three(diff)
                    return final
                elif len(diff) == 4:
                    final = temp+" "+four(diff)
                    return final
                elif len(diff) == 5:
                    final = temp+" "+five(diff)
                    return final
            else: 
                return temp
    elif int(num[5])<int(num[0]):
        if num[0] == "1":
            temp = "99999"
        else:
            temp = str(int(num[0])-1)+"9999"+str(int(num[0])-1)
        diff = str(int(num)-int(temp))
        if diff != "0":
            if len(diff) == 2:
                final = temp +" "+two(diff)
                return final
            elif len(diff) == 1:
                final = temp +" "+ diff
                return final
            elif len(diff) == 3:
                final = temp+" "+three(diff)
                return final
            elif len(diff) == 4:
                final = temp+" "+four(diff)
                return final
            elif len(diff) == 5:
                final = temp+" "+five(diff)
                return final
            elif len(diff) == 6:
                final = temp+" "+six(diff)
                return final
        else: 
            return temp
        
def generate_num(num):
    if len(str(num)) == 1:
        return num
    if len(str(num)) == 2:
        return two(num)
    if len(str(num)) == 3:
        return three(num)
    if len(str(num)) == 4:
        return four(num)
    if len(str(num)) == 5:
        return five(num)
    if len(str(num)) == 6:
        return six(num)
    if len(str(num)) == 7:
        return "999999 1"

# Main program 
choice = ""
again = "y"
while again != "n":
    while choice == "":
        choice = int(input("Enter the number here: "))            
    print("The palindromic sums are:", generate_num(choice))
    again = (input("Do you want to run the program again? (y/n)" ))
    choice = ""
print("Thank you for using the program!")