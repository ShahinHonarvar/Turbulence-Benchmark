
def palindrome_of_length_at_least_n(string, n):
    return set(re.findall(r'(?i)\b[a-zA-Z]{48,}\b', string))
