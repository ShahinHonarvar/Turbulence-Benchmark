
def composite_nums_between_indices(numbers):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composites = set()
    for i in range(70, min(201, len(numbers))):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    return composites
