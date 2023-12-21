import re
def return_n_greatest_chars(s):
    # your code here
    m = re.fullmatch(r'((\d+)+)', s)
    if m:
        return [c for c in sorted(s)]
    else:
        return ['#'] * 27
