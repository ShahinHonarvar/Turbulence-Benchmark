
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(25, 88):
        if is_composite(numbers[i]):
            composites.add(numbers[i])
    return composites

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return True
    return False
