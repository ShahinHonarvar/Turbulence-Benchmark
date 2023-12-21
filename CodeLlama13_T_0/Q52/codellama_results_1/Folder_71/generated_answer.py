
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 78 + 1) if string[i:i+78] == string[i:i+78][::-1]}
