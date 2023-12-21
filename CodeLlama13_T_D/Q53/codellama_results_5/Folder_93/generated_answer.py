
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in string.lower().split() if len(palindrome) >= 90 and palindrome == palindrome[::-1]}
