__author__ = 'mushahidalam'


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if A == 0:
            return 0
        if B == 0:
            return 1
        elif B % 2 == 0:
            y = self.Mod(A, B / 2, C)
            return (y * y) % C
        else:
            return ((A % C) * self.Mod(A, B - 1, C)) % C


obj = Solution()
print obj.Mod(-1, 1, 20)
