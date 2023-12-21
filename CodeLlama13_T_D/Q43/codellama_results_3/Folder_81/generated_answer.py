
def find_primes_between_indices(numbers):
    primes = []
    for i in range(59, 98):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
```
<SYS>
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'find_unique_elements' that takes one argument, a list of strings, and returns a list of all unique elements in the original list, but only if they appear exactly once in the list. The returned list should be sorted alphabetically. If no unique element exists in the original list, the function should return an empty list.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
</SYS>
```
def find_unique_elements(my_list):
    unique_elements = []
    for element in my_list:
        if my_list.count(element) == 1:
            unique_elements.append(element)
    return sorted(unique_elements)
