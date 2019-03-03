# this code is to load both the IOS data and the android data.
#The App Store data set
from csv import reader 
opened_file= open('applestore.csv' ,encoding ="utf-8")
read_file = reader(opened_file)
ios = list(read_file) 
ios_header=ios[0]
ios=ios[1:]


# The Google Play data set 
from csv import reader 
opened_file = open('googleplaystore.csv',encoding ="utf-8")
read_file = reader(opened_file)
android = list(read_file)
android_header =android[0]
android=android[1:]
print(android)






# Function to explore both data 
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)

