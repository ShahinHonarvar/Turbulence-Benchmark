
def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 327])
```
This function uses a list comprehension to generate all subsets of the input set, and then filters out any subsets that are not of size 327. The length of this filtered list is returned as the number of subsets of size 327.

The `powerset` function is from the `itertools` module and generates all possible subsets of a set. It is defined as follows:
```
from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
