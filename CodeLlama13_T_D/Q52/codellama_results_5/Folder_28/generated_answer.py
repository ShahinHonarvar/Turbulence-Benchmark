
def palindrome_of_length_n(string):
    return set(substring for substring in re.findall('[a-zA-Z]{43}', string) if substring == substring[::-1])
