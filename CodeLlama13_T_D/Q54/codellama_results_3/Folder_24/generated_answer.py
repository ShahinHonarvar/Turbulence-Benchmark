
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_prime' that takes an argument which is a positive integer. The function should return True if the argument is prime and False otherwise. A prime number is a positive integer greater than 1 that is divisible only by itself and 1.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
Here is a text specification delimited by angle brackets. Create  code according to the text specification. <Write a function called 'is_right_truncatable_prime' that takes an argument which is a positive integer. The function should return True if the argument is a right-truncatable prime number and False otherwise. A right-truncatable prime number is a prime number that remains prime when the last rightmost digit is successively removed.> The  code should be delimited only by triple backticks. Do not add comments to your code. Generate only one solution without any explanation.
```
def is_right_truncatable_prime(n):
    if n <= 1:
        return False
    while n > 10:
        if not is_prime(n % 10):
            return False
        n //= 10
    return is_prime(n)
