from Q34.codellama_results_1.Folder_37.generated_answer import find_original_set


def test_one_element_similar_sets():
    l = []
    for i in range(67):
        l.append({1})
    assert find_original_set(*l) == {1}


def test_distinct_one_element_sets():
    l = []
    for i in range(67):
        l.append({i})
    assert find_original_set(*l) == set(range(67))


def test_similar_sets():
    l = []
    for i in range(67):
        l.append(set(range(10)))
    assert find_original_set(*l) == set(range(10))


def test_distinct_sets():
    l = []
    for i in range(0, 67*67, 67):
        l.append(set(range(i, i + 67)))
    assert find_original_set(*l) == set(range(67*67))


def test_several_subsets():
    l = []
    for i in range(67):
        l.append(set(range(i+1)))
    assert find_original_set(*l) == set(range(67))
