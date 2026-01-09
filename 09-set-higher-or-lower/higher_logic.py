#importing choice function from random module and game data from custom module
from random import choice
from higher_game_data import data


#function to get a random data
def get_data():
    
    data_object = choice(data)
    return data_object
    

#method to check who has the highest follower count and display the data in a formatted way
def checking_data(object1, object2):
    
    #collecting data for profile 1
    name = object1["name"]
    follower_count = object1["follower_count"]
    description = object1 ["description"]
    country = object1["country"]
    higher_profile = ""
    
    #collecting data for profile 2
    name2 = object2["name"]
    follower_count2 = object2["follower_count"]
    description2 = object2 ["description"]
    country2 = object2["country"]

    #if statement
    if follower_count > follower_count2:
        higher_profile = "profile1"
    else:
        higher_profile = "profile2"
        
    return higher_profile      
