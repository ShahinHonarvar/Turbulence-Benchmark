import re
def all_even_ints_exclusive(nums):
    return [x for x in range( 389, 749) if re.match(r'(0|2)[0-9]', str(x))]
