import re
def palindrome_of_length_at_least_n(s):
    return re.findall(r'(?=([^aieou]))(.)(?!([^aieou]))\1', s.lower())
