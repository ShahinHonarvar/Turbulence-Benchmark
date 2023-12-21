import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=.)(a|b|c|d|e|f|g|h)(?=.)(a|b|c|d|e|f|g|h)(?=.)(a|b|c|d|e|f|g|h)(?=.)(a|b|c|d|e|f|g|h)(?=.)(a|b|c|d|e|f|g|h)', s[1:-1]))
