
def sum_odd_ints_inclusive(my_list):
    odd_sum = 0
    for i in range(8):
        if my_list[i] % 2 == 1:
            odd_sum += my_list[i]
    return odd_sum
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'filter_long_words' that takes one argument, a list of strings, and returns a new list containing only the strings from the original list that are longer than 5 characters.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def filter_long_words(my_list):
    return [word for word in my_list if len(word) > 5]
