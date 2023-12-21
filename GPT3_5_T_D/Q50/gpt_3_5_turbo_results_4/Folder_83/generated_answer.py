
def if_contains_anagrams(lst):
    count = 0

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                count += 1
                if count >= 48:
                    return True

    return False
