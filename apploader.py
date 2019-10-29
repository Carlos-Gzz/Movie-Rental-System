from user import User

import json

user = User("Carlos")

user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")

with open("Carlos", "w") as f:
    json.dump(user.json(), f)
