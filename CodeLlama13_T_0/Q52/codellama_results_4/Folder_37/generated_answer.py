
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 84 + 1) if string[i:i+84].isalpha() and string[i:i+84] == string[i:i+84][::-1]}
