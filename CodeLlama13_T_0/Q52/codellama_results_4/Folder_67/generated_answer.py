
def palindrome_of_length_n(string):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{42}', string) if len(palindrome) == 42 and palindrome == palindrome[::-1]}
