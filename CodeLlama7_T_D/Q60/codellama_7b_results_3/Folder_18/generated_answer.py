
def all_left_right_truncatable_prime(x):
   # Initialize an empty list to store the prime numbers
   prime_numbers = []

   # Iterate from 1 to x
   for i in range(1, x + 1):

       # Check if i is a prime number
       if is_prime(i):

           # Check if i is left-and-right-truncatable prime number
           if is_left_right_truncatable_prime(i):

               # Add i to the list of prime numbers
               prime_numbers.append(i)

   # Return the list of prime numbers sorted in descending order
   return sorted(prime_numbers, reverse=True)

def is_left_right_truncatable_prime(n):
   # Initialize a boolean variable to store the result
   result = True

   # Check if n contains 0
   if '0' in str(n):

       # Set result to False
       result = False

   # Check if n is a prime number
   if not is_prime(n):

       # Set result to False
       result = False

   # Return the value of result
   return result

def is_prime(n):
   # Initialize a boolean variable to store the result
   result = True

   # Check if n is less than 2
   if n < 2:

       # Set result to False
       result = False

   # Check if n is divisible by any number between 2 and sqrt(n)
   for i in range(2, int(n ** 0.5) + 1):

       # Check if n is divisible by i
       if n % i == 0:

           # Set result to False
           result = False

   # Return the value of result
   return result
