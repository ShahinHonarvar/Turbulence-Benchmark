
def palindrome_of_length_n(string, n):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{83}', string) if len(palindrome) == n}
