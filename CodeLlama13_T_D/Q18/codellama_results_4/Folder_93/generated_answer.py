
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(86, 90):
        if lst[i] % -61 == 0 or lst[i] % -79 == 0:
            sum += lst[i]
    return sum
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'reverse_string' that takes one argument, a string, and returns the reversed string. If the input string is not a string data type, it should raise a TypeError with an appropriate message.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return "".join(reversed(s))
