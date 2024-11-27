from true_math import divide as tm
from fake_math import  divide as fm

def main():
    num1 = 69
    num2 = 0

    result1 = fm(num1, 3)
    result2 = fm(3, num2)
    result3 = tm(49, 7)
    result4 = tm(15, num2)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
if __name__ == '__main__':
    main()