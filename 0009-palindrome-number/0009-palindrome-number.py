class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        else:
            org_no = x
            rev_no = 0
            while x!=0:
                last_digit = x %10
                rev_no = rev_no *10+ last_digit
                x//=10
        return  org_no ==  rev_no      