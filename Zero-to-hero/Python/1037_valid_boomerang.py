class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        from decimal import Decimal
        x0 = points[0][0]
        x1 = points[1][0]
        x2 = points[2][0]
        y0 = points[0][1]
        y1 = points[1][1]
        y2 = points[2][1]
        if [x0,y0] == [x1,y1] or [x1, y1] == [x2, y2]:
            return False
        if x0 == x1:
            if x1 == x2:
                return False
            else: 
                return True
        if y0 == y1:
            if y1 == y2:
                return False
            else:
                return True

        k = (y1 - y0) / (x1 - x0)
        b = (y0 - k * x0)
        if y2 == round(k*x2 + b, 2):
            return False
        else:
            return True