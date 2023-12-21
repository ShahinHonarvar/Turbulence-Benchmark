
def palindromes_of_specific_lengths(s):
    s = s[:11].lower()
    output = set()
    for l in range(3,6):
        for i in range(len(s) - l + 1):
            substring = s[i:i+l]
            if substring == substring[::-1] and substring.isalpha():
                output.add(substring)
    return output
