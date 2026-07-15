# 1-Import random module 
import random

# 2-Create list of subject
subjects = [
    "Sharukh Khan",
    "Virat Kohli",
    "Nirmala Sithraman",
    "Narendra Modi(P.M. of India)",
    "A Mumbai Cat",
    "A group of Monkeys",
    "Auto Rickshaw Driver",
    "A famous scientist",
    "A chef",
    "A school principle",
    "The H.O.D. of KIOT Department"
]

# Creating list of actions
actions = [
    "launches missile",
    "cancels",
    "dance with Melony",
    "eats",
    "declares war on",
    "orders the children",
    "celebrates",
    "wins the final",
    "punishes the students",
    "is playing with kid's toys"
   
]

# Creating list of places
places = [
    "at Red Fort",
    "in Mumbai Local Train",
    "in a plate of samosa",
    "inside the paliaments",
    "at Ganga Ghat",
    "during IPL matches",
    "at India Gate",
    "in the college campus",
    "at India-Pakistan Border",
    "in Russia"
]

# start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS : {subject} {action} {place}"
    print("\n" + headline )
    user_input = input("\n Do you want another headline ?? (yes/no)  ").strip().lower()

    if user_input == "no":
        break

print("\n Thanks for using the Fake News Generator .Have a good day .")