# Tests — DSA-Recursion-Patterns
# Run: pytest tests/ -v

def test_subsets():
    result = subsets([1,2,3])
    assert len(result) == 8   # 2^3
    assert [] in result
    assert [1,2,3] in result

def test_n_queens():
    assert len(n_queens(1)) == 1
    assert len(n_queens(4)) == 2
    assert len(n_queens(8)) == 92

def test_permutations():
    result = permutations([1,2,3])
    assert len(result) == 6   # 3!
    assert [1,2,3] in result

def test_hanoi():
    moves = hanoi(3, moves=[])
    assert len(moves) == 7  # 2^3 - 1