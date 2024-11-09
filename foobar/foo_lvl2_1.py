# Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their toes. But you've noticed a flaw in the algorithm -- it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 

# You have worked out that the algorithm has the following process: 

# 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
# 2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
# 3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
# 4) Assign n = z to get the next minion ID, and go back to step 2

# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

# Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.

# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution('210022', 3)
# Output:
#     3

# Input:
# Solution.solution('1211', 10)
# Output:
#     1

# def get_descending_order(num):
#     # num_str = str(num)  # Convert the number to a string
#     digits = list(num)  # Convert the string to a list of digits
#     digits.sort(reverse=True)  # Sort the digits in descending order
#     descending_num = int(''.join(digits))  # Convert the sorted digits back to an integer
#     return descending_num

# def get_ascending_order(num):
#     # num_str = str(num)  # Convert the number to a string
#     digits = list(num)  # Convert the string to a list of digits
#     digits.sort()  # Sort the digits in ascending order
#     ascending_num = int(''.join(digits))  # Convert the sorted digits back to an integer
#     return ascending_num

# def base_10(int_base_n, n):
#     x=list(int_base_n[::-1])
#     y_base_10=0
#     for i,a in enumerate(x):
#         y_base_10+=int(a)*(n**i)
#     return str(y_base_10)

# def change_base(n, b):
#     residual=int(n)
#     digits_base_n=[]
#     while residual >=len(n):
#         r=residual%int(n)
#         digits_base_n.append(str(r))
#         residual=(residual-r)//b
#     digits_base_n.append(str(residual))
#     return ''.join(digits_base_n[::-1])


# def solution(n, b):
#     k = len(n)
#     m = n
#     mini_id = []
#     while m not in mini_id:
#         mini_id.append(m)
#         s = sorted(m)
#         x_descend = ''.join(s[::-1])
#         y_ascend = ''.join(s)        
#         if b == 10:
#             int_m = int(x_descend) - int(y_ascend)
#             m = str(int_m)
#         else:
#             int_m_10=int(base_10(x_descend,b))-int(base_10(y_ascend,b))
#             m=change_base(str(int_m_10),b)

#         m=(k-len(m))*'0'+m
#     print(mini_id)
#     return len(mini_id) - mini_id.index(m)

# Example usage:

# Convert decimal number `d` to base `b`
def dTob(d,b):
    digits=[]
    while d>0:
        digits.insert(0,str(d%b))
        d=d//b
    return ''.join(digits)

# Convert number `b` from base `c` to decimal
def bTod(b,c):
    n=0
    for d in str(b):
        n=c*n+int(d)
    return n

# Perform subtraction `x - y` in base `b`
def negative(x,y,b):
    if b==10:
        return int(x)-int(y)
    
    dx=bTod(x,b)
    dy=bTod(y,b)
    dz=dx-dy
    return dTob(dz,b)

def solution(n,b):
    #list to store encountered numbers
    arr=[]
    while True:
        #convert minion_id_desc to a string, sort in descending order
        minion_id_desc = "".join(sorted(str(n), reverse=True))
        #convert minion_id_asce to a string, sort in ascending order
        minion_id_asce = "".join(sorted(str(n)))
        #Performing the subtraction x - y in base b
        z = negative(minion_id_desc,minion_id_asce,b)

        z2=len(str(z))
        i2=len(str(minion_id_desc))

        # If lengths of k and i are different add leading zeros to k to maintain length i2
        if (z2)!=i2:
            z=z*pow(10,(i2-z2))

        for index, item in enumerate(arr):
            if item==z:
                return index+1
        #Add k to the list of encountered numbers & set n as the new value k for the next iteration
        arr=[z]+arr
        n=z

n = '1211'
b = 10
result = solution(n, b)
print(result)


