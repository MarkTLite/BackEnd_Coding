import random
while True:
    try:
        a,b = random.randint(0,20), random.randint(0,20)
        c = a*b
        print("What is {}*{} ?".format(a,b))
        x = int(input(">"))

        if(x==c):
            print("Correct!")
        else:
            print("Stupid")

    except ValueError:
        print("Wrong input")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              