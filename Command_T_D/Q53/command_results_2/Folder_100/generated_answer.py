def palindrome_of_length_at_least_n(s):
    return set(s.lower().findall("(" + "".join(str(c) for c in range(ord('a') - 1, ord('z') + 1)) + ")" + str(i) for i in range(1, n + 1)))
