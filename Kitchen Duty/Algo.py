import array

#for Breakfast duty the loop will have to go three times
houses = ['JapanHouse','CalgaryHouse','EastHouse','MCLHouse','VicHouse']
int a
int room_name=0
data = []
break_fast = []
for a in houses:
    HouseName = a
    floor = true #for 1st
    if(floor==true):
        floor_name = "1st"
        room_name = 1
    else:
        floor_name = "2nd"
        room_name = 6
     #have to index or we can put all the room no and put it in loop such that if status of one room members is false then it will move till it find next
    #here we will be taking from table of room 8
    def switch_room(room_name):
        with open ("../HouseName/floor_name/Room+room_name.xls","r") as file:
            for line in file:
                data.append(line)
            return data
    

    RoomArray = switch_room(room_name)# it will receive eg J8
    temp = RoomArray[0]#it will give 1std from the array J8
        for()
         if(temp[3]=='true'):
            break_fast.append(student1)
            temp[3] = 'false'
    else:
       
    floor = false
    room_name = room_name+1






    