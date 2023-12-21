
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    composites_set = set()
    for i in range(10, 101):
        if is_composite(numbers[i]):
            composites_set.add(numbers[i])

    return composites_set
