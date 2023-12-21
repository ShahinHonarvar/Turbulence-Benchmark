
def if_perfect_num(numbers):
    def is_perfect_num(num):
        if num <= 1:
            return False
        divisors_sum = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        return divisors_sum == num
    
    return is_perfect_num(numbers[194])
