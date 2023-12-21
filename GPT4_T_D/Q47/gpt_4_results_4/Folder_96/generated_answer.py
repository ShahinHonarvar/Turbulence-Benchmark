
def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    found_palindromes = set()

    for from_index in range(len(s)):
        for to_index in range(from_index + 50, min(from_index + 101, len(s) + 1)):
            substring = s[from_index:to_index]
            if substring == substring[::-1] and substring.isalpha():
                found_palindromes.add(substring)

    return found_palindromes
