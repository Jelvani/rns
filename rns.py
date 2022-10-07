import sympy
import z3
import numpy as np

'''
Residue number system implementation
'''

class rns:
    def __init__(self,num,bases):
        if (type(num) != int) and (type(num) != list):
            raise TypeError("Number must be a decimal integer or in RNS form")

        if type(num) == list:
            if not all(isinstance(n, int) for n in num) and len(num) == len(bases):
                raise TypeError("RNS residues in incorrect format")
            self.residues = num
            self.dec = None

        elif type(num) == int:
            self.residues = [num % m for m in bases]
            self.dec = num

        self.bases = bases

    @property
    def get_decimal(self):
        if not self.dec:
            self.dec = self.__to_dec()
        return self.dec

    @property
    def get_residues(self):
        return self.residues


    #convert residues to decimal form using CRT
    def __to_dec(self):
        s = z3.Solver()
        x = z3.Int('x')
        for idx in range(len(self.bases)):
            s.add((x%self.bases[idx]) == self.residues[idx])
        s.check()
        return s.model()[x].as_long()
        


    def __add__(self,b):
        if not isinstance(b,rns):
            raise TypeError(f"cannot add non-residue type '{type(b)}'")
        if self.bases != b.bases:
            raise TypeError("Numbers must be of same bases")
        return rns([((self.residues[idx] + b.residues[idx] ) % self.bases[idx]) for idx in range(len(self.bases))], self.bases)

    def __sub__(self,b):
        if not isinstance(b,rns):
            raise TypeError(f"cannot subtract non-residue type '{type(b)}'")
        if self.bases != b.bases:
            raise TypeError("Numbers must be of same bases")
        return rns([((self.residues[idx] - b.residues[idx] ) % self.bases[idx]) for idx in range(len(self.bases))], self.bases)

    def __neg__(self):
        return rns((np.array(self.bases) - np.array(self.residues)).tolist(), self.bases)

    def __mul__(self,b):
        if not isinstance(b,rns):
            raise TypeError(f"cannot multiply non-residue type '{type(b)}'")

        if self.bases != b.bases:
            raise TypeError("Numbers must be of same bases")
        return rns([((self.residues[idx] * b.residues[idx] ) % self.bases[idx]) for idx in range(len(self.bases))], self.bases)

    def __eq__(self, b):
        if isinstance(b,rns):
            return (self.residues == b.residues and self.bases == b.bases)
        return False

    def __str__(self):
        return str(self.residues)
        


if __name__ == "__main__":
    mods = list(sympy.primerange(0, 500))
    a = rns(12,mods)
    b = rns(34,mods)
    print(a == a)