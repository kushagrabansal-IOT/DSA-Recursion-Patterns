# Learning Notes — DSA-Recursion-Patterns

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

## Complexity Reference

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Subsets | O(2^n · n) | O(n) | 2^n subsets |
| Permutations | O(n! · n) | O(n) | Swap-backtrack |
| N-Queens | O(n!) | O(n) | With pruning |
| Tower of Hanoi | O(2^n) | O(n) | Optimal: 2^n-1 moves |
| Flood Fill DFS | O(m·n) | O(m·n) | Grid size |
| Fibonacci (memo) | O(n) | O(n) | vs O(2^n) naive |