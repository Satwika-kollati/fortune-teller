print("Welcome to Kollati Satwika's Fortune Teller (21JE0474)!")

mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("You’re radiating joy! Keep smiling and share that vibe.")
elif mood == "sad":
    print("Every storm runs out of rain—stay strong, brighter days are ahead.")
elif mood == "neutral":
    print("Even the quiet days hold potential, Satwika! Stay open to new surprises.")
else:
    print("Choose from happy/sad/neutral moods")