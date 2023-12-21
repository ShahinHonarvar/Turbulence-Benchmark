
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall(r'\b[a-zA-Z]{26,}\b', string) if palindrome == palindrome[::-1]}
