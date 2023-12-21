
def composite_nums_between_indices(lst):
    composites = set()
    for num in lst[4:5]:
        if num < 2:
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                composites.add(num)
                break
    return composites
