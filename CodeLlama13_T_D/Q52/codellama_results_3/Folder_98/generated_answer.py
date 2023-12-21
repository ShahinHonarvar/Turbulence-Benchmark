
def palindrome_of_length_n(string):
    return set(s for s in (string[i:j] for i in range(len(string)) for j in range(i + 6, len(string) + 1)) if s == s[::-1])
