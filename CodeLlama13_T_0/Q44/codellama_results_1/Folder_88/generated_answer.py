
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(8, 10):
        if numbers[i].isdigit():
            composites.add(int(numbers[i]))
    return composites
