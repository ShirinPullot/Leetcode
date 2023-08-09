class Solution:
    def mySqrt(self, x: int) -> int:
        n=0
        i=1
        while (x-i) >=0:
            x -=i
            i+=2
            n+=1
        return n
                
        