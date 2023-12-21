
def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 801])
```
This function uses a list comprehension to generate all subsets of the input set `elements`, and then filters out the ones that are not of size 801. The length of this filtered list is returned as the result.

The `powerset` function is defined as follows:
```
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
