
def insert_before_character(string):
    return "".join([char if char != "a" else "a" + char for char in string])
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'insert_after_character' that takes one argument, a string, and returns a string that is identical except that character 'z' has been inserted immediately after any occurrences of character 'z'.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def insert_after_character(string):
    return "".join([char if char != "z" else char + "z" for char in string])
