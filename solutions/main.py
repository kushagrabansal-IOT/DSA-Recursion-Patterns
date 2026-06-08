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