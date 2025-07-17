def is_pallin(num1):
    j = len(num1)-1
    i=0
    while(i<j):
        if num1[i]!=num1[j]:
            return False
        i +=1
        j -=1
    return True

def to_rm(num1):
    size=len(num1)
    j = size-1
    i=0
    while(i<j):
        if num1[i]== num1[j]:
            i+=1
            j-=1
        else:
            str1 = num1[0:i]+num1[i+1:size]
            str2 = num1[0:j]+num1[j+1:size]
            if is_pallin(str1):
                print(num1[i])
                return True
            elif is_pallin(str2):
                print(num1[j])
                return True 
            else:
                return False
    return True

n = input("Enter:")
if to_rm(n):
    print("Is pallindrome")
else:
    print("No")