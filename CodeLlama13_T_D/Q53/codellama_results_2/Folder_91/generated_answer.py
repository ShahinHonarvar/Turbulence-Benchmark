
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)(.)\1+', s))
