
def prime_factors(mylist):
    return set(prime_factorization(mylist[67]))
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_prime' that takes one argument, an integer, and returns True if it is a prime number or False otherwise.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
