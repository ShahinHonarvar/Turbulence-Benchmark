
def if_contains_anagrams(lst):
    def count_anagrams(string):
        count = 0
        for i in range(len(lst)):
            if sorted(string.lower()) == sorted(lst[i].lower()) and len(lst[i]) >= 3:
                count += 1
        return count

    total_count = 0
    for i in range(len(lst)):
        total_count += count_anagrams(lst[i])

    if total_count <= 416:
        return True
    else:
        return False
