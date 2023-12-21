
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in string.split() if len(palindrome) >= 100 and palindrome == palindrome[::-1]}
