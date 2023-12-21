
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    all_palindromes = set()

    for i in range(len(s)):
        for j in range(i+66, len(s)+1):
            sub_str = ''.join(char for char in s[i:j] if char.isalpha())
            if sub_str == sub_str[::-1]:
                all_palindromes.add(sub_str)

    return all_palindromes
