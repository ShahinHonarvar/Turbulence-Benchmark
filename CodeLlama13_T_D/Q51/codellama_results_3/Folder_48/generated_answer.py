
def if_contains_anagrams(my_list):
    anagrams = []
    for s in my_list:
        s = s.lower()
        if len(s) >= 3 and not (any(s[i] == s[j] for i in range(len(s)) for j in range(i+1, len(s)))):
            anagrams.append((s, ''.join(sorted(s))))
    return len(anagrams) <= 277
