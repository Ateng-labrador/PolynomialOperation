from src import polynomial, Operation



# x^2 + 6x + 8


term13 = polynomial.PrintOperation(coeff=8, exp=0)
term12 = polynomial.PrintOperation(coeff=6, exp=1, next_node=term13)
term11 = polynomial.PrintOperation(coeff=1, exp=2, next_node=term12)

# 5x^2 + 7x + 9

term23 = polynomial.PrintOperation(coeff=9, exp=0)
term22 = polynomial.PrintOperation(coeff=7, exp=1, next_node=term23)
term21 = polynomial.PrintOperation(coeff=5, exp=2, next_node=term22)




res = Operation.Operation(term21.chain(), term11.chain())
print(res.multyply())
