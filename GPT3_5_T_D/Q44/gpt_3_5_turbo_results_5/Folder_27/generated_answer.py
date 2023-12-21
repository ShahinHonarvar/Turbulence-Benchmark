
def composite_nums_between_indices(lst):
    prime = [False] * (max(lst) + 1)
    composites = set()

    for num in lst:
        if num > 1:
            prime[num] = True

    for i in range(2, int(max(lst) ** 0.5) + 1):
        if prime[i]:
            for j in range(i * 2, max(lst) + 1, i):
                prime[j] = False

    for i in range(22, 64):
        if prime[lst[i]] is False:
            composites.add(lst[i])

    return composites
