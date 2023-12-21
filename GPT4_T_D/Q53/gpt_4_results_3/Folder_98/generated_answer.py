
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for size in range(6, length+1):
        for start in range(0, length-size+1):
            chunk = s[start:start+size]
            if chunk == chunk[::-1]:
                palindromes.add(chunk)
    return palindromes
