import re
def palindromes_between_indices(s):
    return re.findall(r'(?i)(?=([^aieou]))([aieou])([aieou])([aieou])([aieou])([aieou])([aieou])', s)
