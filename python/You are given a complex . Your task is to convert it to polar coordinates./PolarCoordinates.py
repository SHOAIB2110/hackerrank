import cmath
c=complex(input())
print(abs(complex(c.real,c.imag)))
print(cmath.phase(complex(c.real,c.imag)))
