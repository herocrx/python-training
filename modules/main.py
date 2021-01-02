
#import algorithms.fibonnaci
from algorithms import fibonnaci


def main():
    #print('Simple module import usage: ', algorithms.fibonnaci.calculate(100))
    print('Simple module import usage: ', fibonnaci.calculate(57))

if __name__ == "__main__":
    main()