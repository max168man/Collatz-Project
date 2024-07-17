import sys
import math

mlist = []  # declare a list of integers


def verify(x: int, s: str) -> bool:
    arr = s
    orgX = x

    if (x < 1) or not (str(float(x)).endswith('.0')): 
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

        if int(arr[i]) in {0, 1}:
            if str(float(y)).endswith('.0') and y >= 1:
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


def recursiveFor(n: int, l: int, origN: int, j: int, qj: int, Y_k: int):
    if n > 1:
        for x in range(0, l + 1)[::-1]:
            mlist.append(x)
            recursiveFor(n - 1, l, origN, j, qj, Y_k)
            mlist.pop(origN - n)
    else:
        for x in range(0, l + 1)[::-1]:
            mlist.append(x)
            accept = True
            for i in range(0, origN - 1):
                if mlist[i] < mlist[i + 1]:
                    accept = False
                    break
            if accept:
                sum = 0
                for i in range(0, origN):
                    sum += math.pow(2, mlist[i]) * math.pow(3, i + 1)
                collatzNum = ((math.pow(2, j - qj) * Y_k) - sum) / math.pow(3, qj)
                binStr = ""
                for i in range(0, len(mlist))[::-1]:
                    if mlist[i] == 0:
                        binStr = "1" + binStr
                    else:
                        if i == (len(mlist) - 1):
                            for t in range(0, mlist[i]):
                                binStr = "0" + binStr
                            binStr = "1" + binStr
                        else:
                            if mlist[i] == mlist[i + 1]:
                                binStr = "1" + binStr
                            else:
                                for t in range(0, mlist[i] - mlist[i + 1]):
                                    binStr = "0" + binStr
                                binStr = "1" + binStr

                for t in range(0, j - 2 - len(binStr)):
                    binStr = "0" + binStr
                if verify(collatzNum, binStr):
                    print("Correct Collatz number ", collatzNum)
                    print("BVC code: ", binStr)
                    mlist.pop()

with open('nums.txt', 'w') as file:
    for k in range(1, 50):
        for j in range(1, 50):
            print(f"k={k}, j={j}")
            Y_k = math.pow(2, 2 * k) - 1

            if j < 2:
                continue

            for qj in range(1, j):
                if qj == 1:
                    continue
                    x = math.pow(2, j - 1) * Y_k / 3
                    binStr = "0" * (j - 2)
                    if verify(x, binStr):
                        print(f"Correct Collatz number for k={k}, j={j}, qj={qj}: ", x)
                        print("BVC code: ", binStr)
                        1 + 1

                if qj == 2:
                    continue
                    for i in range(0, j - 2):
                        x = (math.pow(2, j - 2) * Y_k - math.pow(2, i) * 3) / 9
                        binStr = ""
                        for t in range(0, j - 2):
                            if t == i:
                                binStr = "1" + binStr
                            else:
                                binStr = "0" + binStr
                        if verify(x, binStr):
                            print(f"Correct Collatz number for k={k}, j={j}, qj={qj}: ", x)
                            print("BVC code: ", binStr)
                            1 + 1

                if qj == j - 1:
                    continue
                    sum = 0
                    for i in range(1, j - 3):
                        sum += math.pow(3, i)
                    x = (2 * Y_k - sum) / math.pow(3, j - 1)
                    binStr = "1" * (j - 2)
                    if verify(x, binStr):
                        print(f"Correct Collatz number for k={k}, j={j}, qj={qj}: ", x)
                        print("BVC code: ", binStr)
                        1 + 1

                if qj == j - 2:
                    #print(f"Case: qj == j - 2 for k={k}, j={j}, qj={qj}")
                    for m in range(0, j - 2):
                        sum1 = 0
                        sum2 = 0
                        for i in range(1, m + 1):
                            sum1 += 2 * math.pow(3, i)
                        for i in range(m + 1, j - 2):
                            sum2 += math.pow(3, i)
                        x = (4 * Y_k - (sum1 + sum2)) / math.pow(3, j - 2)
                        if m == 0:
                            binStr = "0" + "1" * (j - 2)
                        else:
                            binStr = "1" * (j - 2 - m - 1) + "0" + "1" * m
                        if x % 1 == 0:
                            file.write(f"Case qj == j - 2: k={k}, m={m}, j={j}, yk={Y_k}, qj={qj}, binStr={binStr}: {x}\n")    
                        if x % 1 == 0:
                            if verify(x, binStr):
                                print("---------------------------------------")
                                print(f"Correct Collatz number for k={k}, m={m}, j={j}, qj={qj}: ", x)
                                print("---------------------------------------")
                                print("BVC code: ", binStr)
                                file.write(f"Correct Collatz number for k={k}, m={m}, j={j}, qj={qj}: {x}\n")

                if 2 < qj < j - 2:
                    continue
                    recursiveFor(qj - 1, j - qj - 1, qj - 1, j, qj, Y_k)
                    mlist.clear()