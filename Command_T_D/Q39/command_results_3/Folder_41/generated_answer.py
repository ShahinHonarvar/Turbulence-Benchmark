import sys
def return_n_greatest_chars(s):
    if not s:
        return []
    lst = [c for c in s if ord(c) > ord(max(s))]
    return sorted(lst[:37])
