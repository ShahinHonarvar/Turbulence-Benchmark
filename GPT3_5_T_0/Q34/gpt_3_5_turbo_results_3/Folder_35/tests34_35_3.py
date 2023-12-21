from Q34.gpt_3_5_turbo_results_3.Folder_35.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(702):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(702):
        l.append({i})
    assert find_original_set(*l) == set(range(702))


def test_similar_sets():
    l = []
    for i in range(702):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 702*702, 702):
        l.append(set(range(i, i + 702)))
    assert find_original_set(*l) == set(range(702*702))


def test_several_subsets():
    l = []
    for i in range(702):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(702))
