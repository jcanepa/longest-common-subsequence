'''
Find the length of the longest common subsequence
using a recursive approach.
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


if __name__ == '__main__':
    A = ['b', 'd']
    B = ['a', 'b', 'c', 'd']
    print(
        lcs_recursive(A, B))