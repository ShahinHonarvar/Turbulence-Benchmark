
def if_perfect_num(numbers):
    for i in range(len(numbers)):
        if i == 80:
            num = numbers[i]
            sum_divisors = 0
            for d in range(1, num):
                if num % d == 0:
                    sum_divisors += d
            if sum_divisors == num:
                return True
            else:
                return False
