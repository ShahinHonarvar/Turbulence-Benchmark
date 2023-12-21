
def composite_nums_between_indices(numbers):
    composites = set()
    for number in numbers[1:2]:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    composites.add(number)
                    break
    return composites
