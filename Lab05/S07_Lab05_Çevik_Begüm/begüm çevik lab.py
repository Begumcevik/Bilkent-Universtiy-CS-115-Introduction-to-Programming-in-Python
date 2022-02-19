
d={}
filehandle = open('restaurants (1).txt','r')
for line in filehandle : 
    line = line[:-1]
    pos = line.split(',')
    stars = pos[0]
    name = pos[1] 
    num= pos[2:]
    if stars not in d:
             
        d[stars] = [(name,num)]
    else:
        d[stars].append((name,num))
        
            
print("1) Find by Restaurant")
print("2) Find by Rating")
print("3) EXIT")
choice = int(input("Choice: "))

while choice != 3 :
    if choice == 1 :
        restaurant_name = input("Enter the restaurant name: ")
        for k in d:
            for n in d[k]:
                if n[0] == restaurant_name : 
                    print(restaurant_name, "phone number are" ,n[1])
    elif choice == 2 :
        rating = input("Enter rating to search: ")
        for k in d:
            if rating == k :
                for n in d[k]:
                    print(n[0],n[1])
    else: 
        print("Invalid!!")
    
    print("1) Find by Restaurant")
    print("2) Find by Rating")
    print("3) EXIT")
    choice = int(input("Choice: "))
            

filehandle.close()