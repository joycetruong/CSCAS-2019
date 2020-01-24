import array
#japan house room 8 boys
std1 = ['Lakpa','1st Year','Nepal','true']
std2 = ['Danik','2nd Year','Canada','true']
std3 = ['Daniel','2nd Year','Columbia','true']
std4 = ['Rohan','1st Year','Kenya','true']
J8 = [std1,std2,std3,std4]
#japan house room 6 girls
std1 = ['Bella','2nd Year','Australia','true']
std2 = ['Lara','1st Year','Turkey','true']
std3 = ['Emily','1st Year','Canada','true']
std4 = ['Vicky','1st Year','Canada','true']
J6 = [std1,std2,std3,std4]
#Vic house room 1 boys
std1 = ['Ram','1st Year','Switzerland','true']
std2 = ['Shyam','2nd Year','Moroco','true']
std3 = ['Sonam','2nd Year','Bhutan','true']
std4 = ['Routian','1st Year','China','true']
V1 = [std1,std2,std3,std4]
#Vic house room 8 girls
std1 = ['Naomi','1st Year','HongKong','true']
std2 = ['Sakurako','1st Year','Japan','true']
std3 = ['psycho','2nd Year','Canada','true']
std4 = ['Mental','2nd Year','Mexico','true']
V8 = [std1,std2,std3,std4]
#Calgary room 7 boys
std1 = ['Ritsuki','1st Year','Japan','true']
std2 = ['Donovan','2nd Year','Canada','true']
std3 = ['Giovany','1st Year','Venzuela','true']
std4 = ['Thomas','1st Year','Greenland','true']
C7 = [std1,std2,std3,std4]
#Calgary room 3 girls
std1 = ['Agnes','1st Year','Cameroon','true']
std2 = ['Emily','1st Year','Canada','true']
std3 = ['Sky','1st Year','China','true']
std4 = ['Bishakha','2nd Year','USA','true']
C3 = [std1,std2,std3,std4]
Houses = ['JapanHouse','VicHouse','CalgaryHouse','EastHouse','MclHouse']
Breakfast = []
#for Breakfast duty the loop will have to go three times
int a
for(a:Houses):
    gender = true #for boys
    RoomNo = 8 #have to index or we can put all the room no and put it in loop such that if status of one room members is false then it will move till it find next
    #here we will be taking from table of room 8
    def switch_room(RoomNo):
            return a[0]+RoomNo
    
    if(gender==true):
        RoomArray = switch_room(RoomNo)# it will receive eg J8
        temp = RoomArray[0]#it will give 1std from the array J8
        if(temp[3]=='true'):
            Breakfast.append(student1)
            temp[3] = 'false'
    else:
        RoomArray = switch_room(RoomNo)
        temp = RoomArray[0]#it will give 1std from the array J8
        if(temp[3]=='true'):
            Breakfast.append(student1)
            temp[3] = 'false'
    gender = false
    RoomNo = RoomNo+1






    