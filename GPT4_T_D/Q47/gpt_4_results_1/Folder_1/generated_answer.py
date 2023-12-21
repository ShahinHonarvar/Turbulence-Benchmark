
def palindromes_of_specific_lengths(string):
    string = string[15:90]
    filtered_string = ''.join(e for e in string if e.isalnum())
    palindromes_set = set()
    for i in range(len(filtered_string)):
        for j in range(i+40, min(i+73, len(filtered_string) + 1)):
            possible_palindrome = filtered_string[i:j]
            if possible_palindrome == possible_palindrome[::-1]:
                palindromes_set.add(possible_palindrome.lower())
    return palindromes_set
