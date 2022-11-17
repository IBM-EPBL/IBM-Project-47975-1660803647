i=0
while(i==0):
    temp=int(input("Enter the temperature:"))
    hum=int(input("Enter the humidity:"))
    if(temp>38):
     print("Alarm Detected! Temperature is high")
    else:
     print("Reached Normal Temperature:)")
    break