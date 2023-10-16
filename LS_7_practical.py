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

#List

list = [1,3,5,4,6]
squares = []
while list:
    squares.append((list.pop())**2)
print(squares)


list1 = [1,3,5,4,6,8,9]
index = 0
while index < len(list1):
    element = list1[index]
    if element % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
    index += 1


list2 = ['James','Joe','Makarand','Jenny','SeeyaRam']
index = 0
while index < len(list2):
    element = list2[index]
    print(len(element))
    index += 1
