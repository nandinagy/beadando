def det2x2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

matrix = [
    [ 4, 2, 2 ],
    [ 3, 7, 1 ],
    [ 9, 5, 7 ]
]
print("Matrix:")
for array in matrix: print(array)
print()

a,b,c = matrix[0]

efhi = [x[1:] for x in matrix[1:]]
dfgi = [x[::2] for x in matrix[1:]]
degh = [x[0:2] for x in matrix[1:]]

det = (
    a * det2x2(efhi)
    - b * det2x2(dfgi)
    + c * det2x2(degh)
)

print(f"A matrix determinansa: {det}")
