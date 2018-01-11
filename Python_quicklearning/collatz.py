import sys

def collatz(number):

        print(number)
        if number == 1:
                sys.exit()
        elif number % 2 == 0:
                t = number // 2
                collatz(t)
        else :
                t = 3 * number + 1
                collatz(t)


num = int(input("please input a integer: "))
collatz(num)
