
def all_left_right_truncatable_prime(x):
   # Initialize an empty list to store the prime numbers
   prime_numbers = []

   # Iterate from 1 to x (inclusive)
   for i in range(1, x + 1):
       # Check if the number is a prime number
       if is_prime(i):
           # Check if the number is left-and-right-truncatable prime
           if is_left_right_truncatable_prime(i):
               # Add the prime number to the list
               prime_numbers.append(i)

   # Sort the list in descending order
   prime_numbers.sort(reverse=True)

   # Return the sorted list of prime numbers
   return prime_numbers

# Check if a number is a prime number
def is_prime(n):
   # If the number is less than 2, it is not prime
   if n < 2:
       return False

   # Check if the number is divisible by any integer between 2 and the square root of the number
   for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False

   # If the number passes all the checks, it is prime
   return True

# Check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):
   # If the number is not prime, it is not left-and-right-truncatable prime
   if not is_prime(n):
       return False

   # Check if the number contains 0

   if '0' in str(n):
       return False

   # Remove the leading leftmost and last rightmost digits of the number

   leading_leftmost = int(str(n)[1:])
   last_rightmost = int(str(n)[:-1]))

   # Check if the number is prime after removing the leading leftmost and last rightmost digits

   if not is_prime(leading_leftmost) or not is_prime(last_rightmost):
       return False

   # If the number passes all the checks, it is left-and-right-truncatable prime

   return True
