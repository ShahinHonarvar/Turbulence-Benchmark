
def if_perfect_num(numbers):
    if numbers[162]:
        for i in range(1, int(numbers[162]**0.5) + 1):
            if numbers[162] % i == 0:
                return True
        return False
    else:
        return False
