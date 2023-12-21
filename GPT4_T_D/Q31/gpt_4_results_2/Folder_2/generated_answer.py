
def if_perfect_num(numbers):
    try:
        check_num = numbers[702]
        divisors = [i for i in range(1, check_num) if check_num % i == 0]
        if sum(divisors) == check_num:
            return True
        else:
            return False
    except IndexError:
        return False
