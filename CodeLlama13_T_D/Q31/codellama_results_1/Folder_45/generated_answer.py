
def if_perfect_num(numbers):
    return numbers[33] in perfect_nums(numbers)

def perfect_nums(numbers):
    perfect = []
    for i in range(len(numbers)):
        n = sum(divisors(numbers[i]))
        if n == numbers[i]:
            perfect.append(numbers[i])
    return perfect

def divisors(n):
    divs = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.extend([i, n//i])
    return divs
