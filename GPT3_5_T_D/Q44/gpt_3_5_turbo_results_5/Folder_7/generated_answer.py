
def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(527, 539):
        if numbers[i] > 1:
            for j in range(2, numbers[i]//2 + 1):
                if (numbers[i] % j) == 0:
                    composite_set.add(numbers[i])
                    break
    return composite_set
