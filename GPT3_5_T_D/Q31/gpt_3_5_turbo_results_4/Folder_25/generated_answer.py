
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if num // i != i:
                    divisors.append(num // i)
        return sum(divisors) == num

    return is_perfect(numbers[90])
