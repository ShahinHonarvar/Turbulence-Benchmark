
def composite_nums_between_indices(lst):
    def is_composite(n):
        factors = [f for f in range(2,n) if n % f == 0]
        return True if len(factors) > 0 else False

    composite_numbers = set([num for num in lst[4:5] if is_composite(num)])
    return composite_numbers
