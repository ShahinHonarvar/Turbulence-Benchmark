
def if_perfect_num(numbers):
    def is_perfect_num(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    return is_perfect_num(numbers[56])
