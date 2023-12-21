
def palindrome_of_length_at_least_n(s):
    s = "".join(ch.lower() for ch in s if ch.isalpha())
    n, result_set = 55, set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            segment = s[i:j]
            if segment == segment[::-1]:
                result_set.add(segment)
    return result_set
