
def if_perfect_num(numbers):
    def is_perfect(number):
        divisors = []
        for i in range(1, number):
            if number % i == 0:
                divisors.append(i)
        return sum(divisors) == number
    
    if len(numbers) >= 7 and is_perfect(numbers[6]):
        return True
    else:
        return False
