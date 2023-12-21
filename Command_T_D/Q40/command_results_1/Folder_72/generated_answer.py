import re
def return_n_smallest_chars(s):
    m = re.match(r'<Write a function called "return_n_smallest_chars" that takes one argument, a string of distinct characters and creates a list of exactly 37 characters of the given string that have the smallest ASCII values. The function should sort the list in descending order and returns the list.>(\S*)', s)
    if m:
        s = m.group(1)
        sm = set(s)
        return sorted(sm)[-37:]
    else:
        return []
