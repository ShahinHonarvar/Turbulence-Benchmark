
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and lst[i].lower() != lst[j].lower():
                if is_anagram(lst[i].lower(), lst[j].lower()):
                    pairs.append((lst[i], lst[j]))

    if len(pairs) <= 181:
        return True
    else:
        return False
