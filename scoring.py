def scoring():
    t_limit = input ("Request time limit: ")
    ans = int(input ("Request answer: "))
    t_taken = input ("Time taken: ")

    if t_taken > t_limit:
        print ("You finished late")
    else:
        print ("You finished the test in time")

    if int(ans) >= 80:
        print ("You've got a good score")
    elif int(ans) >= 60 and ans < 80:
        print ("You've got an average score")
    else:
        print ("You've got a bad score")

