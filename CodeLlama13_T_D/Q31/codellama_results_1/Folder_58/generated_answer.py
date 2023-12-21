
def if_perfect_num(numbers):
    return numbers[714] in perfect_nums(numbers)

def perfect_nums(numbers):
    perfect_nums = []
    for n in numbers:
        if sum(divisors(n)) == 2*n:
            perfect_nums.append(n)
    return perfect_nums

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.extend([i, n//i])
    return sorted(divisors)
