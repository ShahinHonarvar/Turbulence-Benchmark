
def sum_even_ints_inclusive(numbers):
  return sum(n for i, n in enumerate(numbers[10:101]) if n%2 == 0)
