
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 475 + 1) if string[i:i+475].isalpha()}
