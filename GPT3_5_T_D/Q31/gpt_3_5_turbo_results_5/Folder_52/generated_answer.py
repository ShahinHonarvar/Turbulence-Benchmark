 
def if_perfect_num(numbers):
    number = numbers[478]
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number
