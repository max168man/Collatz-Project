import sys
import math

mlist = []  # declare a list of integers
count = 0  # total number of BVC's created

def verify(x: int, s: str) -> bool:
    arr = s
    orgX = x

    if (x < 1) or not str(float(x)).endswith('.0'):
        return False

    if str(float(x)).endswith('.0'):
        if str(math.log(x, 2)).endswith('.0'):
            return False
    else:
        return False

    for i in range(len(arr) - 1, -1, -1):
        if int(arr[i]) == 1:
            y = 3 * x + 1
        else:
            y = x / 2

        if int(arr[i]) == 1 or int(arr[i]) == 0:
            if str(float(y)).endswith('.0') and (y >= 1):
                if str(math.log(y, 2)).endswith('.0'):
                    return False
                else:
                    if int(arr[i]) == 1 and y % 2 != 0 and x % 2 == 0:
                        return False
            else:
                return False
        else:
            return False
        x = y
    return True

# This is a function for a nested for-loop with variable depth n.
def recursiveFor(n: int, l: int, origN: int, j: int, qj: int, Y_k: int):
    global count
    if n > 1:  # skip the last loop; leave it for termination
        for x in range(0, l + 1)[::-1]:
            mlist.append(x)
            recursiveFor(n - 1, l, origN, j, qj, Y_k)
            mlist.pop(origN - n)
    else:
        print(f"else clause: l: {l}, mlist: {mlist}, j: {j}, qj: {qj}, Y_k: {Y_k}, origN: {origN}")
        for x in range(0, l + 1)[::-1]:
            mlist.append(x)
            accept = True
            for i in range(0, origN - 1):
                if mlist[i] < mlist[i + 1]:
                    accept = False
                    break
            if accept:
                sum = 0
                print(f"Calculating with params - mlist: {mlist}, origN: {origN}, j: {j}, qj: {qj}, Y_k: {Y_k}")
                for i in range(0, origN):
                    sum = sum + math.pow(2, mlist[i]) * math.pow(3, i + 1)
                collatzNum = ((math.pow(2, j - qj) * Y_k) - sum) / math.pow(3, qj)
                print(f"collatNum: {collatzNum}")
                binStr = ""
                for i in range(0, len(mlist))[::-1]:
                    if mlist[i] == 0:
                        binStr = "1" + binStr
                        print("case mlist[i] = 0 (recursiveFor) BVC code: ", binStr)
                    else:
                        if i == (len(mlist) - 1):
                            for t in range(0, mlist[i]):
                                binStr = "0" + binStr
                            binStr = "1" + binStr
                            print("i = ", i, " len mlist = ", len(mlist))
                            print("case i == (len(mlist) - 1) (recursiveFor) BVC code: ", binStr)
                        else:
                            if mlist[i] == mlist[i + 1]:
                                binStr = "1" + binStr
                                print("case mlist[i] == mlist[i + 1] (recursiveFor) BVC code: ", binStr)
                            else:
                                for t in range(0, mlist[i] - mlist[i + 1]):
                                    binStr = "0" + binStr
                                binStr = "1" + binStr
                                print("case else (recursiveFor) BVC code: ", binStr)

                for t in range(0, j - 2 - len(binStr)):
                    binStr = "0" + binStr  # length of BVC is j-2
                    
                print("Final zero addition BVC code: ", binStr)
                count += 1
                if verify(collatzNum, binStr):
                    pass
            mlist.pop()

k = int(input("Enter the value of k, which determines the root of a subtree: "))
print("k is:", k)

j = int(input("Enter the value of the j-th stair in the tree rooted at Y_k/3: "))
print("j is:", j)

Y_k = math.pow(2, 2 * k) - 1

if j < 2:
    print("j is less than 2")
    sys.exit()

for qj in range(1, j):
    if qj == 1:
        x = math.pow(2, j - 1) * Y_k / 3
        binStr = ""
        for t in range(1, j - 1):
            binStr = binStr + "0"
        print("BVC code: ", binStr)
        count += 1
        if verify(x, binStr):
            pass

    if qj == 2:
        for i in range(0, j - 2):
            x = (math.pow(2, j - 2) * Y_k - math.pow(2, i) * 3) / 9
            binStr = ""
            for t in range(0, j - 2):
                if t == i:
                    binStr = "1" + binStr
                else:
                    binStr = "0" + binStr
            print("BVC code: ", binStr)
            count += 1
            if verify(x, binStr):
                pass

    if qj == j - 1:
        sum = 0
        for i in range(1, j - 3):
            sum = sum + math.pow(3, i)
            x = (2 * Y_k - sum) / math.pow(3, j - 1)
            binStr = ""
            for t in range(1, j - 1):
                binStr = binStr + "1"
            print("BVC code: ", binStr)
            count += 1
            if verify(x, binStr):
                pass

    if qj == j - 2:
        for m in range(0, j - 2):
            sum1 = 0
            sum2 = 0
            for i in range(1, m + 1):
                sum1 = sum1 + (2 * math.pow(3, i))
            for i in range(m + 1, j - 2):
                sum2 = sum2 + math.pow(3, i)
            x = (4 * Y_k - (sum1 + sum2)) / math.pow(3, j - 2)

            if m == 0:
                binStr = ""
                binStr = "0"
                for t in range(1, j - 2):
                    binStr = binStr + "1"
            else:
                binStr = ""
                for t in range(m + 1, j - 2):
                    binStr = "1" + binStr
                binStr = "0" + binStr
                for t in range(1, m + 1):
                    binStr = "1" + binStr
                print("BVC code: ", binStr)
                count += 1
            if verify(x, binStr):
                pass

    if 2 < qj < j - 2:
        recursiveFor(qj - 1, j - qj - 1, qj - 1, j, qj, Y_k)
        mlist.clear()

print("Total BVCs generated:", count)
