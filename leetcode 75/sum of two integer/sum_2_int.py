class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = (tmp) & mask
            
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)