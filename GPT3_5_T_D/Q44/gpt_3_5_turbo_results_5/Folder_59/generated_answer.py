
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(0, 10):
        num = numbers[i]
        is_composite = False
        for j in range(2, num):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            composites.add(num)
    return composites
