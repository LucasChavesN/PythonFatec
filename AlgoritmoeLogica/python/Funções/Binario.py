from re import A


def convert(a,b,c,d):
    a = a * 2**3
    b = b * 2**2
    c = c * 2**1
    d = d * 2**0

    return(a+b+c+d)

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print("Binario para decimal: ",convert(a,b,c,d))
main()