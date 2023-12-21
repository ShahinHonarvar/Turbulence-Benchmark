
def palindrome_of_length_at_least_n(string, n):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{21,}', string) if len(palindrome) >= n}
