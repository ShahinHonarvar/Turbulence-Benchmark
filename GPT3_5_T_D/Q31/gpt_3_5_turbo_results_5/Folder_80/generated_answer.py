
def if_perfect_num(numbers):
    def is_perfect_num(num):
        if num <= 1:
            return False
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        divisors_sum = sum(divisors)
        return divisors_sum == num

    if len(numbers) > 746:
        return is_perfect_num(numbers[746])
    return False
