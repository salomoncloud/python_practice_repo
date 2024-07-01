username = input("username: ")
password = input("password: ")
password_length = len(password)
hidden_password = "*" * password_length # here you take the length of your password and convert it all to stars
print(f"{username}, your password {hidden_password} is {password_length} letters long")