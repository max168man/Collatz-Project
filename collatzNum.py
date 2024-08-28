import math

mlist = [1, 2, 3, 1]
def calculate_collatz_num(mlist, origN, j, qj, Y_k):
    total_sum = 0
    for i in range(0, origN):
        total_sum += math.pow(2, mlist[i]) * math.pow(3, i + 1)
    
    collatz_num = ((math.pow(2, j - qj) * Y_k) - total_sum) / math.pow(3, qj)
    
    return collatz_num