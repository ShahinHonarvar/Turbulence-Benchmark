
def composite_nums_between_indices(lst):
    composites = set()
    for i in range(20, 201):
        num = lst[i]
        isComposite = True
        if num < 2:
            isComposite = False
        else:
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    isComposite = False
                    break
        if isComposite:
            composites.add(num)
    return composites
