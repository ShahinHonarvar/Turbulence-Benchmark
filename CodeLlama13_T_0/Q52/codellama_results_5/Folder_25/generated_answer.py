
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 90 + 1) if string[i:i+90].isalpha() and string[i:i+90] == string[i:i+90][::-1]}
