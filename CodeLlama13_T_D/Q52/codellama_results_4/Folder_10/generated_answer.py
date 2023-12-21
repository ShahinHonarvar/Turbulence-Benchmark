
def palindrome_of_length_n(string):
    return {pal for i in range(len(string) - 53) for pal in (string[i:i+54] if len(string[i:i+54]) == 54 and string[i:i+54].lower() == string[i:i+54][::-1].lower() else '')}
