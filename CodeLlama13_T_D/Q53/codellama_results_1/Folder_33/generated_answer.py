
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in string if len(palindrome) >= 141 and palindrome == palindrome[::-1]}
