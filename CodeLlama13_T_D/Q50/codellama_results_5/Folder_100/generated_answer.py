
def if_contains_anagrams(strs):
    count = 0
    for s in strs:
        for t in strs:
            if s.lower() != t.lower():
                if ''.join(sorted(s)) == ''.join(sorted(t)):
                    count += 1
    return count >= 95
