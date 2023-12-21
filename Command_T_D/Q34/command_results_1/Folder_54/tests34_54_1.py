from Q34.command_results_1.Folder_54.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(74):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(74):
        l.append({i})
    assert find_original_set(*l) == set(range(74))


def test_similar_sets():
    l = []
    for i in range(74):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 74*74, 74):
        l.append(set(range(i, i + 74)))
    assert find_original_set(*l) == set(range(74*74))


def test_several_subsets():
    l = []
    for i in range(74):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(74))
