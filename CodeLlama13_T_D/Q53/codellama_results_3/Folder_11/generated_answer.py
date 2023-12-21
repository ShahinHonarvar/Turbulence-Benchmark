
def palindrome_of_length_at_least_n(string):
    return {pal for pal in set(re.findall(r'(?i)\b[a-z]{54,}\b', string)) if pal == pal[::-1]}
