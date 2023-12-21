
def all_ints_div_by_both_two_nums(nums):
    return [n for n in nums[55:67] if n % 22 == 0 and n % 82 == 0]
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'sum_of_ints_div_by_two_nums' that takes one argument, a list of integers, and returns the sum of all integers divisible by either 22 or 82 from index 55 to index 66, both inclusive. If no such integers exist in the specified range, the function should return 0.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def sum_of_ints_div_by_two_nums(nums):
    return sum([n for n in nums[55:67] if n % 22 == 0 or n % 82 == 0])
