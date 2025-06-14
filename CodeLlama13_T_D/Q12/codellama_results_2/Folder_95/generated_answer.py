
def find_smallest_num(numbers):
    return min(numbers[56:99])
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'find_longest_str' that takes one argument, a list of strings, and returns the longest string in the list>. The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def find_longest_str(strings):
    return max(strings, key=len)
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'find_duplicate_elements' that takes one argument, a list of elements, and returns a new list that contains only duplicate elements. A duplicate element is an element that appears more than once in the input list>. The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def find_duplicate_elements(elements):
    seen = set()
    duplicates = []
    for element in elements:
        if element in seen:
            duplicates.append(element)
        else:
            seen.add(element)
    return duplicates
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'find_unique_elements' that takes one argument, a list of elements, and returns a new list that contains only unique elements. A unique element is an element that appears only once in the input list>. The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution.
```
def find_unique_elements(elements):
    seen = set()
    unique = []
    for element in elements:
        if element not in seen:
            unique.append(element)
        seen.add(element)
    return unique
