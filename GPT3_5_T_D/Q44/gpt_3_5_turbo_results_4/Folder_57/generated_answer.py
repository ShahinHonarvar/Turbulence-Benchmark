
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(25, 60):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    return composites

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return True
    return False
