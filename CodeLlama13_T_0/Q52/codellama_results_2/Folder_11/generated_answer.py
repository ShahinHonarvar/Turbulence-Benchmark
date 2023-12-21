
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 76) if string[i:i+77].isalpha() and string[i:i+77][::-1] == string[i:i+77]}
