password = input("Enter the password to save\n >")

if(input("Input the password")==password):
    print("Authentication success")
else:
    print("Wrong pasword, You have two attempts")
    for i in range(2):
        if(input("Re-Enter Password\n>")!= password):
            if(i==1):
                print("You have Been Blocked out")
                break
            else:
                continue
        else:
            print("Authentication success")
            break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  