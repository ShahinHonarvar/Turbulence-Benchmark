
def palindrome_of_length_at_least_n(string, n):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{27,}', string) if len(palindrome) >= n}
