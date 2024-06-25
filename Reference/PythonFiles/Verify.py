import sys
import math

mlist=[]  # declare a list of integers


def verify(x: int, s: str) -> bool:
    arr=s
    orgX = x

    if ((x < 1) or not(str(float(x)).endswith('.0')) ) : return False     
    
    if str(float(x)).endswith('.0'):
        if (str(math.log(x,2)).endswith('.0')):
            print("Verify: ", x, " is a power of 2!")
            return False
    else:
        print("Verify: ", x, " is not an integer!")
        return False

   # for t in range(len(arr)-1, -1, -1): print("Bit", t, "is ", arr[t])

                

    for i in range(len(arr)-1, -1, -1): # scan from lsb to msb
        print("Here is the bit value of arr[i] ", int(arr[i]))
        if (int(arr[i]) == 1): y = 3*x + 1
        else: y = x/2

        if ((int(arr[i]) == 1) or (int(arr[i]) == 0)):
            # start the verification here
            if str(float(y)).endswith('.0') and (y >= 1):
                if (str(math.log(y,2)).endswith('.0')):
                    print("Verify: ", y, " is a power of 2 while verifying ", orgX)
                    return False
                else:
                    if (int(arr[i]) == 1) and (y %2 !=0) and (x %2 ==0):
                        print("Verify: y = ", y, "is odd and x =", x," is even while verifying ", orgX, "!")
                        return False    
            else:
                print("Verify: y =", y, " is non-integer for x =", x)
                return False
        else:
            print("Verify: Unknown character in the string ", s)
            return False
        x = y
    return True

x = int(input("Enter the value of x, which we will test verify on: "))
print("x is: ", x)

string = str(input("Enter the binary string, which we will test verify on: "))
print("str is: ", string)

boolean: bool
boolean = verify(x, string)


boolean = verify(x, string)

if boolean == True:
    print("x was verified.")
else:
    print("x was not verified.")