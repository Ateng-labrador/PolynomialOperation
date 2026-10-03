from .polynomial import Polynomial

class Operation:
    def __init__(self, poly1, poly2):
        self.poly1 = poly1
        self.poly2 = poly2

    def add(self):
        res = []
        for i in range(len(self.poly1)):
            x = self.poly1[i] + self.poly2[i]
            res.append(x)
        return res

    def subtraction(self):
        res = []
        for i in range(len(self.poly1)):
            res.append(self.poly1[i] - self.poly2[i])
        return res

    def multyply(self):
        m = len(self.poly1)
        n = len(self.poly2)
        res = [0] * (m + n - 1)
        for i in range(m):
            for j in range(n):
                res[i + j] += self.poly1[i] * self.poly2[j]
        return res
        
            


