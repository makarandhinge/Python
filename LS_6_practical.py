#SIMPLE EXAMPLE OF WHILE LOOP

x = 0
i = 1
while(i<=10):
    print(i)
    i+=1


number = 1
total = 0
while(number <= 10):
    total = total + number
   #print(total)
    number +=1
    print(total)

#ELSE STATEMENT IN WHILE LOOP

counter = 0
while(counter <= 4):
    print("Control inside loop")
    counter += 1
else:
    print("Contol inside else")


#Break

i = 1
while(i<=10):
    print(i)
    if(i==7):
        break
    i = i+1

#Continue

i = 1
while(i <= 10):
    i += 1
    if(i == 7):
        print("Loop break")
        continue
    print(i)

