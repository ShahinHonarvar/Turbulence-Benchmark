
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall('[a-zA-Z]{84,}', string) if palindrome == palindrome[::-1]}
