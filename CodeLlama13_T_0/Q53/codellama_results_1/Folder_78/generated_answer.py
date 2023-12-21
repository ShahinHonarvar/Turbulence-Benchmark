
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{96,}', string) if palindrome == palindrome[::-1]}
