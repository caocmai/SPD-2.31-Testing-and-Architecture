# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print(f"{info} was saved into databse")


user_username = input('Please enter your username: ')
save_into_db(user_username)
user_birth_year = int(input('Please enter your birth year: '))
age = 2020 - user_birth_year
print("Hi", user_username, "You are",age, "years old.")
