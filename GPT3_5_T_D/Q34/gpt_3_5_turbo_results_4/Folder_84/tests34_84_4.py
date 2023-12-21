from Q34.gpt_3_5_turbo_results_4.Folder_84.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(132):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(132):
        l.append({i})
    assert find_original_set(*l) == set(range(132))


def test_similar_sets():
    l = []
    for i in range(132):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 132*132, 132):
        l.append(set(range(i, i + 132)))
    assert find_original_set(*l) == set(range(132*132))


def test_several_subsets():
    l = []
    for i in range(132):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(132))
