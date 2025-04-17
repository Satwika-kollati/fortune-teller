import random

print("Welcome to Kollati Satwika's Fortune Teller (21JE0474)!")

# Take user input
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

# Define updated fortunes
fortunes = {
    "happy": [
        "Your joy is a light to everyone around you, Satwika!",
        "Happiness looks amazing on you, Satwika!",
        "Today is shining as bright as your smile, Satwika!"
    ],
    "sad": [
        "It's okay to feel down. This moment will pass.",
        "You’re not alone, Satwika is cheering you on!",
        "Even the darkest clouds can’t hide the sun forever."
    ],
    "neutral": [
        "A calm day can be the perfect reset.",
        "Stay open, small things can lead to big surprises.",
        "Even still waters run deep."
    ],
    "stressed": [
        "Pause. Breathe. You’ve handled tougher days.",
        "Let go of what you can't control—you're doing great.",
        "Remember: one small step at a time is still progress."
    ]
}

# Check mood and print fortune
if mood in fortunes:
    print("Here's your fortune for today:", random.choice(fortunes[mood]))
else:
    print("Sorry, I don't have a fortune for that mood.")