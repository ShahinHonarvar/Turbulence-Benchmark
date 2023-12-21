
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(5, 6):
        num = numbers[i]
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    composites.add(num)
                    break
    return composites
