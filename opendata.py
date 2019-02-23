from csv  import reader 
open_file= open('AppleStore.csv', encoding="utf-8")
read_file = reader(open_file) 
data = list(read_file)
print(data) 
