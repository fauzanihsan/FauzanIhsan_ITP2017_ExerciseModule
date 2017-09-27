import robot
import scoring
x=input("choose program:")

if(x=="robot"):
    robot.robot()
elif(x=="scoring"):
    scoring.scoring()
else:
    print("Program not found.")
