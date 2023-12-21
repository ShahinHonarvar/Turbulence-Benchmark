
def palindrome_of_length_n(s):
    s = s.lower()
    output_set = set()
    for i in range(len(s)):
        for j in range(i):
            sub = s[j:i + 1]
            if len(sub) == 392 and sub == sub[::-1] and sub.isalpha():
                output_set.add(sub)
    return output_set
