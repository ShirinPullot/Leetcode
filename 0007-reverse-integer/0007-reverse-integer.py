class Solution:
    def reverse(self, x: int) -> int:
        min_32bit_int = -2**31
        max_32bit_int = 2**31 - 1
        if x>0:
            x = str(x)
            output = int(x[::-1])
        else:
            x = -1 * x
            x = str(x)
            output = int(x[::-1])*-1
        if min_32bit_int<=output<= max_32bit_int:
            return output
        else:
            return 0
            
        