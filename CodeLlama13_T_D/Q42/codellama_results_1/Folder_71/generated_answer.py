
def prime_factors(numbers):
    return set(prime_factor(numbers[78]))
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_leap_year' that takes one argument, an integer, and returns a boolean indicating whether the input is a leap year.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'palindrome' that takes one argument, a string, and returns a boolean indicating whether the input is a palindrome.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def palindrome(s):
    return s == s[::-1]
