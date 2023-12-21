
def find_largest_num(numbers):
    return sorted(numbers)[52:72][-1]
```
[Inst] < Write a function called 'find_unique' that takes two arguments, an iterable and a callable, and returns the unique elements in the iterable that satisfy the given condition. > The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution. [/Inst]  ```
def find_unique(iterable, condition):
    return list(filter(condition, set(iterable)))
