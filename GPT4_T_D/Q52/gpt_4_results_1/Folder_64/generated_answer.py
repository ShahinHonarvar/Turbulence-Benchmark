
def palindrome_of_length_n(string):
    string = string.lower()
    length = len(string)
    palindrome_set = set()
    for i in range(length):
        for j in range(i+9, length+1):
            substring = string[i:j]
            if subset_palindrome(substring):
                palindrome_set.add(substring)
    return palindrome_set

def subset_palindrome(substring):
    letter_only = ''.join(filter(str.isalpha, substring))  
    return letter_only == letter_only[::-1]
