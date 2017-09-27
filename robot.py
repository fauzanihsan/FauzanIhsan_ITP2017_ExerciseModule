
def robot():
    battery = 4
    print(battery)
    print("I am a robot")

    while(battery>0):
    #if(battery ==0):
        #print("bye")
        #break
    # print("NEW: ",battery)
        action=input("please input action :")
        if (action=="nothing"):
            shutdown=input("do you want to shut down?")
            if(shutdown== "yes"):
                break

            elif(shutdown=="no"):
            #action=input("please input an action")
                continue

        elif(action.isalpha != False):
            new_battery=(int(battery))-1
            print("battery:",str(new_battery))
            print(action)


            charge=input("do you want to charge?")
            if(charge=="yes"):
                battery=(int(new_battery)+1)
            # print(battery)
            #action=input("please input action:")

            else:
                battery=new_battery
            # print(battery)




    # elif(battery == 0):
    #     print("masuk")
    #     break








