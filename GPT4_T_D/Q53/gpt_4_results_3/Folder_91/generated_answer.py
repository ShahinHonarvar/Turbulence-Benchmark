
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s)):
        for j in range(i+7, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                if s[i:j].isalpha():
                    result_set.add(s[i:j])
    return result_set
