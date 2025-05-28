import pytest
from lab1 import TextGraph



# 测试用例1：节点不存在
def test_node_not_found(setup_graph):
    word1 = "non_existent"
    result = setup_graph.calc_shortest_path(word1)
    assert result == f"{word1} not found in graph!"


# 测试用例2：单源最短路径（所有可达节点）
def test_single_source_shortest_path(setup_graph):
    word1 = "a"
    result = setup_graph.calc_shortest_path(word1)

    expected_paths = {
        "b": "Shortest path from a to b: a -> b (length: 1)",
        "c": "Shortest path from a to c: a -> b -> c (length: 2)",
        "d": "Shortest path from a to d: a -> b -> c -> d (length: 3)"
    }

    for target, path in expected_paths.items():
        assert path in result, f"预期路径 '{path}' 未找到"


# 测试用例3：两点间存在路径
def test_shortest_path_between_two_nodes(setup_graph):
    word1 = "a"
    word2 = "c"
    expected = "Shortest path from a to c: a -> b -> c (length: 2)"
    result = setup_graph.calc_shortest_path(word1, word2)
    assert result == expected


# 测试用例4：两点间无路径
def test_no_path_exists(setup_graph):
    word1 = "a"
    word2 = "e"  # 假设e不可达
    result = setup_graph.calc_shortest_path(word1, word2)
    assert result == f"No path exists from {word1} to {word2}!"


# 测试用例5：无权图的路径选择（所有边权重为1）
def test_unweighted_path_selection(setup_graph):
    word1 = "a"
    word2 = "d"
    expected = "Shortest path from a to d: a -> b -> c -> d (length: 3)"
    result = setup_graph.calc_shortest_path(word1, word2)
    assert result == expected


# 测试用例6：单源路径（无边的节点）
def test_single_source_with_no_outgoing_edges(setup_graph):
    word1 = "d"  # d没有出边
    result = setup_graph.calc_shortest_path(word1)
    assert "No paths found from d to other nodes." in result


# 测试用例7：同一节点的路径
def test_same_node_path(setup_graph):
    word1 = "a"
    word2 = "a"
    expected = "Shortest path from a to a: a (length: 0)"
    result = setup_graph.calc_shortest_path(word1, word2)
    assert expected in result, f"预期 '{expected}', 但得到 '{result}'"


# -------------- 测试图结构（无权图） --------------
@pytest.fixture
def setup_graph():
    graph = TextGraph()

    test_text = """
    a b
    b c
    c d
    """

    with open("test_input.txt", "w", encoding="utf-8") as f:
        f.write(test_text)

    graph.build_graph("test_input.txt")

    # 显式添加节点e（无入边和出边）
    graph.nodes.add("e")

    return graph