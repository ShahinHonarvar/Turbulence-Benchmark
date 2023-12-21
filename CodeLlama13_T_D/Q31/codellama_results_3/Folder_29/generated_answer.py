
def if_perfect_num(numbers):
    for i in range(len(numbers)):
        if i == 19:
            num = numbers[i]
            if sum(divisors(num)) == num:
                return True
            else:
                return False

def divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]
