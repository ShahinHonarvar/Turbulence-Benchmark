
def if_perfect_num(numbers):
    return numbers[43] in perfect_nums(numbers)

def perfect_nums(numbers):
    perfect_nums = []
    for i, n in enumerate(numbers):
        divisors = [d for d in range(1, int(n**0.5) + 1) if n % d == 0]
        if sum(divisors) - n == n:
            perfect_nums.append(i)
    return perfect_nums
