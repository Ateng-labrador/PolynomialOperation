
term3 = polynomial.Operation(coeff=8, exp=0)
term2 = polynomial.Operation(coeff=6, exp=1, next_node=term3)
term1 = polynomial.Operation(coeff=1, exp=2, next_node=term2)

print(term1.Quadratic())