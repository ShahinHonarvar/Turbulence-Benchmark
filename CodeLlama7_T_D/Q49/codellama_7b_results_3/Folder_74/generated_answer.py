
def if_decimal_is_divisible(binary_rep):
  # Convert the binary representation string to an integer
  decimal = int(binary_rep, 2)
  # Initialize the Fibonacci sequence with the first two numbers
  fib = [0, 1]
  # Iterate through the Fibonacci sequence until we reach the 166th number
  while len(fib) < 167:
    # Add the next two numbers in the Fibonacci sequence together
    fib.append(fib[-2] + fib[-1])
  # Check if the decimal integer is divisible by the 166th number in the Fibonacci sequence
  return decimal % fib[165] == 0
