
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(262, 747):
        if i < len(numbers):
            num = numbers[i]
            if num > 1:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        composites.add(num)
                        break
    return composites
