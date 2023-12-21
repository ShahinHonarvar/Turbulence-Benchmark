from Q34.gpt_4_results_5.Folder_73.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(19):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(19):
        l.append({i})
    assert find_original_set(*l) == set(range(19))


def test_similar_sets():
    l = []
    for i in range(19):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 19*19, 19):
        l.append(set(range(i, i + 19)))
    assert find_original_set(*l) == set(range(19*19))


def test_several_subsets():
    l = []
    for i in range(19):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(19))
