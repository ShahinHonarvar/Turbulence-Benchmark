
def prime_factors(my_list):
    return set(prime_factors(my_list[733]))
```
<SYS>

Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_unique' that takes one argument, a string, and returns True if the string contains only unique characters, and False otherwise.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
</SYS>
```
def is_unique(s):
    return len(set(s)) == len(s)
