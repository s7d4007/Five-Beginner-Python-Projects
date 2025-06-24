import random

Module_task = [
    "Dive into Streamlit and build a cool interactive app! 🚀",
    "Explore the power of NumPy for lightning-fast calculations 🔢",
    "Master data wrangling with Pandas—turn chaos into clarity 📊",
    "Embark on a TensorFlow journey and create your first neural network 🤖",
    "Unlock the secrets of machine learning with Scikit-learn 🧠",
    "Craft your own web app using Flask—bring your ideas online 🌐",
    "Discover the hidden gems of Python's OS module and automate your workflow 🛠️"
]

Productive = [
    "Try Practicing a BackFlip (Yes, you can do it! 😤)",
    "Do 10 Pushups (Don't be a couch potato 😶)",
    "Do 15 Squats 😫",
    "Do 20 Jumping Jacks 🏃",
    "Hold a 30-second Plank 💪",
    "Do 10 Lunges (each leg) 🦵",
    "Do 15 Sit-ups 🧘",
    "Do 10 Burpees 🤸",
    "Stretch for 5 minutes 🧎",
    "Take a brisk 5-minute walk 🚶"
]

Yoga = [
    "Mountain Pose (Tadasana)",
    "Downward Facing Dog (Adho Mukha Svanasana)",
    "Child's Pose (Balasana)",
    "Cat-Cow Pose (Marjaryasana-Bitilasana)",
    "Cobra Pose (Bhujangasana)",
    "Bridge Pose (Setu Bandhasana)",
    "Seated Forward Bend (Paschimottanasana)",
    "Tree Pose (Vrikshasana)",
    "Easy Pose (Sukhasana)",
    "Legs-Up-The-Wall Pose (Viparita Karani)"
]

Unwind = [
    "Sketch a Portrait ✏️",
    "Count how many tiles are there in your house? 😂",
    "Listen to your favorite song 🎵",
    "Make yourself a cup of tea or coffee ☕",
    "Watch clouds from your window ☁️",
    "Doodle something random 🖊️",
    "Read a page from a book 📖",
    "Take 5 deep breaths and relax 😌",
    "Water your plants 🌱",
    "Write a short poem or haiku 📝",
    "Sit quietly and observe your surroundings 👀",
    "Organize your desk for 2 minutes 🗂️"
]

#Take user_input keeping in mind the error handling. If user puts anthing instead of an integer, a ValueError is thrown saying : Please enter a valid number
try:
    user_input = int(input(("Select Your Theme \n 1. Discover Python Libraries \n 2. Do Something Productive \n 3. Perform Yoga \n 4. Take a Break : \n Enter your response : ")))
    
    if user_input == 1:
        print("Suggested Task : ", random.choice(Module_task))

    elif user_input == 2:
        print("Suggested Task : ", random.choice(Productive))

    elif user_input == 3:
        print("Suggested Task : ", random.choice(Yoga))
        
    elif user_input == 4:
        print("Suggested Task : ", random.choice(Unwind))

    else:
        print("Enter Valid Choice !!!")
        
except ValueError:
    print("Please enter a valid number.")