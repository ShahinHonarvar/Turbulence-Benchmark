
def sum_odd_ints_inclusive(lst):
    return sum(i for i in lst[0:3+1] if i % 2 == 1)
```
<Write a function called 'count_unique_elements' that takes one argument, a list of integers, and returns the number of unique elements in the list. If the list contains no unique elements (i.e., all elements are duplicates), the function should return 0.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def count_unique_elements(lst):
    return len(set(lst))
