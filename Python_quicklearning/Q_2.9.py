State = True
while State:
    spam = input("please input a number:")

    if spam == str(1):
        print("hello")
    elif spam == str(2):
        print("Howdy")
    elif spam == 'q':
        print("programe exit!")
	break
    else:
        print("Greetings!")
