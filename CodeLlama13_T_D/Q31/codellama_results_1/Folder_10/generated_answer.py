
def if_perfect_num(numbers):
    return numbers[54] in perfect_numbers()

def perfect_numbers():
    perfect_nums = []
    for i in range(1, 101):
        if sum(divisors(i)) == i:
            perfect_nums.append(i)
    return perfect_nums

def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
