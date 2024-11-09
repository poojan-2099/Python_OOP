def is_perfect_number(num):
    return sum(int(digit) for digit in str(num)) == 10

def nth_perfect_number(n):
    count = 0
    num = 19  # Start from 19 since it's the first perfect number
    while True:
        if is_perfect_number(num):
            count += 1
            if count == n:
                return num
        num += 9  # Increment by 9 to move to the next potential perfect number


n = 10
for i in range(1,n):
    print(nth_perfect_number(i))  # Output: 28

