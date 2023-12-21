
def all_neg_ints_exclusive(numbers):
    negative_ints = []
    for i in range(42, 87):
        if numbers[i] < 0:
            negative_ints.append(numbers[i])
    return negative_ints
