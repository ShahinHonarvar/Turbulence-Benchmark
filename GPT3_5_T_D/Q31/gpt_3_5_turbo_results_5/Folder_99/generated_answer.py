
def if_perfect_num(numbers):
    num = numbers[733]
    divisors = [1]
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num
