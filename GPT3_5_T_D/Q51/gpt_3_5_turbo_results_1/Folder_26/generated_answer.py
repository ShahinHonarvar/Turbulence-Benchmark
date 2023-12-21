
def if_contains_anagrams(strings):
    pairs_count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and sorted(strings[i].lower()) == sorted(strings[j].lower()):
                pairs_count += 1

    if pairs_count <= 35:
        return True
    else:
        return False
