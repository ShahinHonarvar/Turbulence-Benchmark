
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall(r'(?i)[a-z]{138,}', string) if len(palindrome) % 2 == 0}
