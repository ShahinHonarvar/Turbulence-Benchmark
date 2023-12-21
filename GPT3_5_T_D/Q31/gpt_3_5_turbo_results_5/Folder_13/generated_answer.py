
def if_perfect_num(numbers):
    def is_perfect_number(num):
        divisors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return sum(divisors) == num

    if len(numbers) > 126:
        return is_perfect_number(numbers[126])
    else:
        return False
