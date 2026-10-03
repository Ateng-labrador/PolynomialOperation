import math

class Polynomial:
    # Node Linear
    def __init__(self, coeff, exp, next_node = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next_node

    # read every polynomial
    def chain(self):
        current = self
        equation = []

        while current:
            if current.exp == 0:
                equation.append(current.coeff)
            else:
                equation.append(current.coeff)
            current = current.next
        return equation
    
    def Quadratic(self):
        a = self.chain()[0]
        b = self.chain()[1]
        c = self.chain()[2]

        D = (b**2 - 4 * a * c)
        if D >= 0:
            x1 = (-b + math.sqrt(D))
            x2 = (-b - math.sqrt(D))
            return [x1/(2*a) , x2/(2*a)]
        elif D == 0:
            return [-b/2*a]
        else:   
            x1 = complex((-b/(2*a)),math.sqrt(-D)/(2*a))
            x2 = complex((-b/(2*a)),-math.sqrt(-D)/(2*a))
            return [x1, x2]

class PrintOperation(Polynomial):
    def __init__(self, coeff, exp, next_node=None):
        super().__init__(coeff, exp, next_node)

    def traverse_chain(self):
        current = self
        persamaan = []

        while current:
            if current.exp == 0:
                persamaan.append(f"{current.coeff}")
            else:
                persamaan.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        print(" + ".join(persamaan))
