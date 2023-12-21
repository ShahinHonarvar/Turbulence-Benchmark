
def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for i in range(10):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'get_unique_elements' that takes one argument, a list of integers, and returns a new list containing all unique elements in the original list. If multiple occurrences of an element exist in the original list, only include the first occurrence of that element in the new list.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def get_unique_elements(numbers):
    return list(set((numbers)))
