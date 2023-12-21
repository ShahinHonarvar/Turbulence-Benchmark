
def find_subset_of_length_n(elements, n):
    return len([subset for subset in powerset(elements) if len(subset) == n])
```
<powerset>
```
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
```
<combinations>
```
def combinations(iterable, r):
    "combinations('abc', 3) --> ('abc', 'ab', 'ac', 'ba', 'bb', 'bc')"
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
