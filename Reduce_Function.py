#Without Function
from functools import reduce
from fractions import Fraction
N = int(input())
input_1 = [list(map(int,input().split())) for i in range(0,N)]
Numer = reduce(lambda x,y:x*y, [input_1[i][0] for i in range(len(input_1))])
Denom = reduce(lambda x,y:x*y, [input_1[i][1] for i in range(len(input_1))])
print(Fraction(Numer,Denom).numerator,Fraction(Numer,Denom).denominator)

#With funtion
def product(fracs):
      Numer = reduce(lambda x,y:x*y, [fracs[i].numerator for i in range(len(fracs))])
      Denom = reduce(lambda x,y:x*y, [fracs[i].denominator for i in range(len(fracs))])
      return (Fraction(Numer,Denom).numerator,Fraction(Numer,Denom).denominator)
    

if __name__ == '__main__':
    fracs = []
    for i in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
