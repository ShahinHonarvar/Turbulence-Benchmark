
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        s1 = strings[i]
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if sorted(s1.lower()) == sorted(s2.lower()):
                count += 1

    return count >= 92
