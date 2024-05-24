# import json library
import json

original_data = {

    'name': 'Julia Johnson',
    'age': 21,
    'city': 'Seattle, WA',
    'interests': ['Sleeping', 'Music', 'Reading', 'Traveling'],
    'is_student': True
}
# create and write original data as json file
with open('data.json','w') as json_file:

        json.dump(original_data,json_file,indent=4)

print("Data has been written to data.json")

# reading data.json file and storing it as loaded_data

with open('data.json','r') as json_file:
        
        # creating and giving value to loaded_data variable
        loaded_data = json.load(json_file)

# display text of successfully reading data.json 
print("Succesfully able to read data.json")

# display data of json file
print(loaded_data)

# update key values of loaded_data
loaded_data['age'] = 22
loaded_data['interests'].append('Cooking')

# overwriting data.json file with loaded_data  
with open('data.json','w') as json_file:

        json.dump(loaded_data,json_file,indent=4)

print("Data has been rewritten to data.json")