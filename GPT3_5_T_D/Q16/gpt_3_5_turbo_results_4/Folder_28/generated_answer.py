
def sum_even_ints_inclusive(lst):
    # Get sublist from index 62 to index 63
    sublist = lst[62:64]
    
    # Sum even integers in the sublist
    total = sum(num for num in sublist if num % 2 == 0)
    
    return total if total != 0 else 0
