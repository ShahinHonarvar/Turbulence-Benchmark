def palindrome_of_length_at_least_n(s):
    return set(s.lower().findall("(" + "".join(str(c) for c in range(ord('a'), ord('z') + 1)) + ")") +  # find palindrome starts
             s.lower().findall("(" + "".join(str(c) for c in range(ord('a'), ord('z') + 1)) + ")[-()]"))  # find palindrome ends
