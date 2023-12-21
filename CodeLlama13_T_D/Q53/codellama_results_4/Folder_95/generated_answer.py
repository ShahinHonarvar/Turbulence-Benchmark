
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall(r'[A-Za-z]{35,}', string) if palindrome == palindrome[::-1]}
