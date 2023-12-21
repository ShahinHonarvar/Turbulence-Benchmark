
def all_pos_ints_exclusive(lst):
    return [x for x in lst if 50 < x < 200 and x > 0]
```
[INST:<SYS>]  Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'max_in_list' that takes one argument, a list of integers, and returns the maximum value in the list. If the list is empty, the function should return None>. The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def max_in_list(lst):
    if len(lst) == 0:
        return None
    else:
        return max(lst)
