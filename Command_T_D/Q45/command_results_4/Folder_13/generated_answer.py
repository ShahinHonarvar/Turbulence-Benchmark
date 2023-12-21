import re
def palindromes_between_indices(s):
    m = re.match(r'(.*?)(\D{3}\D{3}\D{3}\D{3}\D{3}\D{3}\D{3}.*?)\1', s)
    return {m.group(1)[:5]] + {m.group(2)[:5]]}
