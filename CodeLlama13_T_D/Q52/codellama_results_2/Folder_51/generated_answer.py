
def palindrome_of_length_n(string):
    return {substring for substring in re.findall("[a-zA-Z]{73}", string) if substring == substring[::-1]}
