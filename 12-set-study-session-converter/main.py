from study_art import logo

#displaying program logo
print(logo)


#prompting user to enter the number of minutes they want to study

user_minutes = int(input("Enter the number of minutes you want to study: "))

#conventing minutes to hours and minutes

hours = user_minutes // 60
minutes = user_minutes % 60


#displaying message 
print(f"You have set a study session for {hours} hour(s) and {minutes} minute(s).")