import pickle

# Define the admin credentials as a dictionary
admin_credentials = {
    "Admin1": "hashed_password1",
    "Admin2": "hashed_password2",
    # Add more admin usernames and hashed passwords as needed
}
# Serialize and save the admin_credentials dictionary to a .pkl file
with open("admin_credentials.pkl", "wb") as file:
    pickle.dump(admin_credentials, file)
