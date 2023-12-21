
def all_left_right_truncatable_prime(x):
  # Initialize an empty list to store the prime numbers
  prime_numbers = []

  # Iterate from 1 to x, checking if each number is a prime number and if it meets the criteria for left-and-right-truncatable prime numbers
  for i in range(1, x + 1):
    # If the current number is not a prime number, continue to the next iteration
    if is_prime(i) == False:
      continue

    # Check if the current number meets the criteria for left-and-right-truncatable prime numbers by removing the leading leftmost and last rightmost digits
    if meets_criteria(i):
      # Add the current number to the list of prime numbers if it meets the criteria
      prime_numbers.append(i)

  return prime_numbers

def is_prime(n):
  # If n is less than or equal to 1, it is not a prime number
  if n <= 1:
    return False

  # Check if any number between 2 and the square root of n is divisible by n
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True

def meets_criteria(n):
  # If the number does not contain any 0s, it is a left-and-right-truncatable prime number
  if "0" in str(n):
    return False

  # Check if the number remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
  for i in range(1, len(str(n))) - 1:
    # If the number is not a prime after removing the leading leftmost digit, it does not meet the criteria for a left-and-right-truncatable prime number
    if is_prime(int(str(n)[i:]))) == False:
      return False

  return True
