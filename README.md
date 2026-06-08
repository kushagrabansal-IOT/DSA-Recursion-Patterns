# DSA-Recursion-Patterns 🔄

[![Python](https://img.shields.io/badge/Language-Python_3.11-3776ab?style=flat&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat)](LICENSE)
[![DSA](https://img.shields.io/badge/Category-DSA-f97316?style=flat)](#)
[![Stars](https://img.shields.io/github/stars/kushagrabansal-IOT/DSA-Recursion-Patterns?style=social)](https://github.com/kushagrabansal-IOT/DSA-Recursion-Patterns)
[![Interview Ready](https://img.shields.io/badge/Interview-Ready-7c3aed?style=flat)](#)

> Master recursion and backtracking — 30+ patterns from basic to advanced. Recursive trees, memoization, tail recursion, call stack visualization.

**Built by [Kushagra Bansal](https://github.com/kushagrabansal-IOT) | Founder @ Project Lab India, Jaipur**

---

## 📌 Topics Covered

| # | Pattern | Problems |
|---|---------|---------|
| 1 | Basic Recursion | Factorial, Fibonacci, Power |
| 2 | Divide & Conquer | Merge Sort, Binary Search |
| 3 | Tree Recursion | Multiple calls per level |
| 4 | Backtracking | N-Queens, Subsets, Permutations |
| 5 | Memoized Recursion | Top-Down DP |
| 6 | Tail Recursion | Optimization technique |

---

## 📋 Problem Statements

### Problem 1 — Generate All Subsets (Power Set)
> Generate all 2^n subsets of a given array.
> `Input: [1,2,3]` → `Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]`

### Problem 2 — N-Queens Problem
> Place N queens on N×N board so no two attack each other.
> `Input: n=4` → `Output: 2 solutions`

### Problem 3 — Generate All Permutations
> Generate all n! permutations of a given array.
> `Input: [1,2,3]` → `Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

### Problem 4 — Flood Fill (DFS Recursion)
> Fill connected region of image with new color.
> `Input: image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2` → `Output: [[2,2,2],[2,2,0],[2,0,1]]`

### Problem 5 — Tower of Hanoi
> Move n disks from source to destination using auxiliary rod.
> `Input: n=3` → `Output: 7 moves printed`

---

## 💻 Solutions + Time & Space Complexity

```python
# DSA-Recursion-Patterns — Core Solutions
# Author: Kushagra Bansal — Project Lab India

def subsets(nums):
    """Generate all subsets using backtracking
    Time: O(2^n · n) | Space: O(n) recursion depth
    """
    result = []
    def bt(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i+1, path)
            path.pop()
    bt(0, []); return result

def n_queens(n):
    """N-Queens backtracking
    Time: O(n!) | Space: O(n)
    """
    res=[]; cols=set(); diag1=set(); diag2=set()
    board=[['.'] * n for _ in range(n)]
    def bt(row):
        if row==n: res.append([''.join(r) for r in board]); return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2: continue
            cols.add(col); diag1.add(row-col); diag2.add(row+col)
            board[row][col]='Q'
            bt(row+1)
            board[row][col]='.'; cols.discard(col); diag1.discard(row-col); diag2.discard(row+col)
    bt(0); return res

def permutations(nums):
    """All permutations via swap-based backtracking
    Time: O(n! · n) | Space: O(n)
    """
    res=[]
    def bt(start):
        if start==len(nums): res.append(nums[:]); return
        for i in range(start, len(nums)):
            nums[start],nums[i] = nums[i],nums[start]
            bt(start+1)
            nums[start],nums[i] = nums[i],nums[start]
    bt(0); return res

def flood_fill(image, sr, sc, color):
    """DFS-based flood fill
    Time: O(m·n) | Space: O(m·n)
    """
    orig = image[sr][sc]
    if orig == color: return image
    def dfs(r, c):
        if not(0<=r<len(image) and 0<=c<len(image[0])): return
        if image[r][c] != orig: return
        image[r][c] = color
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]: dfs(r+dr,c+dc)
    dfs(sr, sc); return image

def hanoi(n, src='A', dst='C', aux='B', moves=[]):
    """Tower of Hanoi — 2^n - 1 moves
    Time: O(2^n) | Space: O(n) stack
    """
    if n==0: return
    hanoi(n-1,src,aux,dst,moves)
    moves.append(f"Move disk {n}: {src} → {dst}")
    hanoi(n-1,aux,dst,src,moves)
    return moves

if __name__ == "__main__":
    print("="*55)
    print("  DSA Recursion Patterns — Project Lab India")
    print("="*55)
    print(f"  Subsets([1,2,3])      = {len(subsets([1,2,3]))} subsets")
    print(f"  N-Queens(4)           = {len(n_queens(4))} solutions")
    print(f"  Permutations([1,2,3]) = {len(permutations([1,2,3]))} perms")
    h=hanoi(3,moves=[])
    print(f"  Hanoi(3)              = {len(h)} moves")
    print("="*55)
```

---

## ⏱️ Complexity Reference Table

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Subsets | O(2^n · n) | O(n) | 2^n subsets |
| Permutations | O(n! · n) | O(n) | Swap-backtrack |
| N-Queens | O(n!) | O(n) | With pruning |
| Tower of Hanoi | O(2^n) | O(n) | Optimal: 2^n-1 moves |
| Flood Fill DFS | O(m·n) | O(m·n) | Grid size |
| Fibonacci (memo) | O(n) | O(n) | vs O(2^n) naive |

---

## 📚 Learning Notes

### 🔑 Key Recursion Insights

1. **Base Case First** — Always identify the terminating condition before writing recursive logic.
2. **Trust the Recursion** — Assume recursive call returns correct result. Don't trace the stack.
3. **Backtracking = Recursion + Undo** — After exploring a path, undo your choice (pop/unset).
4. **Memoization** — If same subproblem appears, cache it. Converts O(2^n) → O(n).
5. **Recursion Tree** — Draw the recursion tree to understand time/space complexity visually.

### 🌳 Backtracking Template
```
def backtrack(state, choices):
    if is_goal(state):
        result.append(copy(state))
        return
    for choice in choices:
        make_choice(state, choice)
        backtrack(state, remaining_choices)
        undo_choice(state, choice)         ← KEY STEP
```

---

## 🎯 Top Interview Questions

1. What is the difference between recursion and iteration? When to prefer each?
2. What is a base case? What happens without one?
3. Explain the call stack. How deep can recursion go?
4. What is tail recursion and why does it matter?
5. How does memoization convert recursion from exponential to polynomial time?
6. What is backtracking? How does it differ from exhaustive search?
7. How do you identify if a problem has optimal substructure?
8. Explain the N-Queens pruning strategy. How does it reduce search space?
9. What is the time complexity of generating all permutations?
10. How would you convert a recursive solution to iterative (using explicit stack)?

---

## ⚠️ Edge Cases to Always Check

- n=0 or n=1 in most recursive problems — verify base case
- Empty input array — handle before recursion
- Very large n — check for stack overflow (Python default 1000)
- Duplicate elements in subsets/permutations — need deduplication
- Disconnected graph/grid in DFS — only floods connected component
- Single cell in flood fill — still works, no recursion needed

---

## 🧪 Test Cases

```python
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
```

---

## 📦 Project Structure

```
DSA-Recursion-Patterns/
├── solutions/
│   ├── main.py
│   ├── backtracking.py      ← N-Queens, Sudoku, Subsets
│   ├── tree_recursion.py    ← Multiple calls per frame
│   └── memoized.py          ← Top-down DP
├── tests/
│   └── test_recursion.py
├── notes/
│   └── recursion_trees.md
└── README.md
```

---

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/kushagrabansal-IOT/DSA-Recursion-Patterns.git
cd DSA-Recursion-Patterns

# Run solutions
python solutions/main.py

# Run tests
python -m pytest tests/ -v
```

---

## 🚀 Future Improvements

- [ ] Add Sudoku solver with constraint propagation
- [ ] Add Word Search II (Trie + Backtracking)
- [ ] Add Cryptarithmetic solver
- [ ] Add visual recursion tree generator
- [ ] Add iterative equivalents using explicit stack

---

## 📄 License

MIT License — Free to use, modify, distribute.

---

## 👨‍💻 Author

**Kushagra Bansal** — Founder @ Project Lab India, Jaipur
🔬 DSA • OOPS • DBMS • IoT • Competitive Programming
🏆 Innovation Award Recipient | IEEE Member
🛒 [radiomarket.in](https://radiomarket.in)

---

> ⭐ **Star this repo** if it helped your interview prep!
> 🍴 **Fork it** — add your own solutions!
> 📢 **Share it** — help other developers!
