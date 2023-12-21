
def if_contains_anagrams(lst):
    def are_anagrams(a, b):
        return sorted(a.lower()) == sorted(b.lower())

    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                count += 1
                if count >= 16:
                    return True
    return False
