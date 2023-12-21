
def if_perfect_num(numbers):
    def is_perfect_num(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    return is_perfect_num(numbers[97])
