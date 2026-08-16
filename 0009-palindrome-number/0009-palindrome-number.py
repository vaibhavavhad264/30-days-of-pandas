class Solution:
    def isPalindrome(self, x) -> bool:
        n = str(x)
        return n == n[ : : -1]
        