
def gcf_two_nums(numbers):
    return _gcf(numbers[90], numbers[84])
```
<Write a function called 'is_perfect_square' that takes one argument, an integer greater than or equal to 1, and returns True if the integer is a perfect square.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_perfect_square(n):
    return n**0.5 == int(n**0.5)
```
<Write a function called 'count_unique_elements' that takes one argument, an iterable of hashable objects, and returns the number of unique elements in the iterable.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def count_unique_elements(iterable):
    return len(set(iterable))
```
<Write a function called 'list_intersection' that takes two arguments, both lists of hashable objects, and returns the intersection of the two lists.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def list_intersection(list1, list2):
    return list(set(list1).intersection(set(list2)))
```
<Write a function called 'count_prime_numbers' that takes one argument, an iterable of integers, and returns the number of prime numbers in the iterable.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def count_prime_numbers(numbers):
    return sum(1 for n in numbers if is_prime(n))
