 
def sum_odd_ints_inclusive(numbers):
    odd_numbers = [n for n in numbers[56:58] if n % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0
