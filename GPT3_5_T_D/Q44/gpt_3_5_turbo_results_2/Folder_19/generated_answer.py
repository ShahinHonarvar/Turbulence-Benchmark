
def composite_nums_between_indices(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    composites = []
    for number in numbers[5:8]:
        if not is_prime(number):
            composites.append(number)

    return set(composites)
