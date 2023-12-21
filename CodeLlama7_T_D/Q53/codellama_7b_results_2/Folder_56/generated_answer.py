
def palindrome_of_length_at_least_n(s, n):
    # Find all substrings that are at least n characters long
    subs = [s[i:i+n] for i in range(len(s)-n+1)]
    # Filter out any substrings that are not palindromes
    palindromes = []
    for sub in subs:
        if sub == sub[::-1]:
            palindromes.append(sub)
    return set(palindromes)
