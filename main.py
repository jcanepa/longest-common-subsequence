'''
Find the length of the longest common subsequence
using a top-down, recursive approach. Runs in exponential time O(2^n),
where n and m are the lenghts of A and B, respectively. Notice the need
for repeated calculations on the same pairs of indices.... we can do better!
'''
def lcs_recursive(A:list, B:list) -> int:
    # one (or more) lists are empty
    if not A or not B:
        return 0
    # matching character found, increment count
    if A[0] == B[0]:
        return 1 + lcs_recursive(A[1:], B[1:])
    # return largest count resulting from either subproblems
    return max(
        lcs_recursive(A[1:], B),
        lcs_recursive(A, B[1:]))

'''
Make the algorithm faster by implementing memorization.
By storing the results of recrusion, duplicated work is eliminated.
Aside from adding a "table", and maintaing idices the strategy remains unchanged.
Approach is still top-down, but table is filled bottom-up.
Takes O(mn) time.
@todo - finish implementation
'''
def lcs_memoization(m, A:list, B:list, i:int=0, j:int=0) -> int:
    # one (or more) lists are empty
    if i == len(A) or j == len(B):
        return 0
    # matching character found, increment count
    if A[i] == B[j]:
        return 1 + lcs_memoization(m, A, B, i+1, j+1)
    # return largest count resulting from either subproblems
    return max(
        lcs_memoization(m, A, B, i+1, j),
        lcs_memoization(m, A, B, i, j+1))

'''
Dynamic programming approach is bottom-up, yet the table is filled top-down.
'''
def lcs_dynamic_programming(A, B) -> int:
    def

if __name__ == '__main__':
    A = ['b', 'd']
    B = ['a', 'b', 'c', 'd']
    # print(lcs_recursive(A, B))

    # create a hash table to keep track of intermediate results:
    # where values can be accessed as m[a_i][b_j]
    m = {}
    print(lcs_memoization(m, A, B))