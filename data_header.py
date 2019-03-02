#This code wil print the data without header 
from csv import reader 
def opened_dataset(file='applestore.csv' ,encoding="utf-8" ,header = True):
     opened_file = open(file)
     read_file = reader(opened_file) 
     data = list(read_file)
#print(data)atings_count = {}
     if header : 
         return data[1:]
     else: 
         return data 
db = opened_dataset()
print(db)

output
runfile('C:/Users/Kangni/mission/appleStore.py', wdir='C:/Users/Kangni/mission')
[['284882215', 'Facebook', '389879808', 'USA', '0', '2974676', '212', '3.5', '3.5', '95', '4+', 'Social ', '37', '1', '29', '1'], ['389801252', 'Instagram', '113954816', 'USA', '0', '2161558', '1289', '4.5', '4', '10.23', '12+', 'Photo & ', '37', '0', '29', '1'], ['529479190', 'Clash of ', '116476928', 'USA', '0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1'], ['420009108', 'Temple ', '65921024', 'USA', '0', '1724546', '3842', '4.5', '4', '1.6.2', '9+', 'Games', '40', '5', '1', '1'], ['284035177', 'Pandora - ', '130242560', 'USA', '0', '1126879', '3594', '4', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']]
