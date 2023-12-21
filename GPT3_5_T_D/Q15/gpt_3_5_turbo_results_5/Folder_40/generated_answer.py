
def sum_odd_ints_inclusive(lst):
    total = 0
    odd_integers = [num for num in lst[0:3] if num % 2 != 0]
    
    if odd_integers:
        total = sum(odd_integers)
    
    return total
