class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch for ch in s if ch.isalnum())
        s=s.lower()
        reverse_s=s[::-1]
        if (s==reverse_s):
            return True
        else:
            return False