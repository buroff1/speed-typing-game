from tkinter import *
import random
from tkinter import messagebox

# Set initial game state variables with clear naming conventions
time_left = 60  # Total time for the game round in seconds
correct_words = 0  # Counter for correct words entered
wrong_words = 0  # Counter for incorrect words entered
i = 0  # Counter for total words processed
sliderwords = ''
count = 0
word_list = [
    'abundance', 'circuit', 'deliberate', 'flamboyant', 'gratitude',
    'hierarchy', 'ignorance', 'juxtapose', 'kaleidoscope', 'luminous',
    'metaphor', 'nostalgia', 'oblivion', 'paradox', 'quintessential',
    'resilience', 'surreal', 'tranquility', 'ubiquitous', 'vibrant',
    'whimsical', 'xenophile', 'yearning', 'zenith',
    'alchemy', 'biome', 'chronicle', 'dystopia', 'euphoria', 'fjord'
]


def timer():
    """Controls the countdown timer for the game session."""
    global time_left, i
    if time_left > 0:
        time_left -= 1
        timerLabel.config(text=time_left)
        timerLabel.after(1000, timer)  # Schedules itself to be called after 1000 milliseconds
    else:
        end_game()  # Calls the function to end the game when timer is up


def end_game():
    """Handles tasks to be done at the end of the game like disabling inputs and calculating results."""
    global time_left, correct_words, wrong_words, i
    wordEntry.config(state=DISABLED)  # Disable the entry widget to stop user input
    result = correct_words - wrong_words
    instruction.config(text=f"Correct words: {correct_words}\nWrong words: {wrong_words}\nTotal Score: {result}")
    instruction.place(x=220, y=550)  # Update instruction label with the results
    update_emojis(result)  # Update emojis based on the score
    if messagebox.askyesno("Play Again?", "Do you want to play again?"):
        reset_game()  # Offer to restart the game


def update_emojis(result):
    """Updates the emoji displayed based on the player's score."""
    # Use conditional statements to set different images for different score thresholds
    if result < 15:
        emoji1Label.config(image=sad)
        emoji2Label.config(image=sad)
    elif result > 15:
        emoji1Label.config(image=happy)
        emoji2Label.config(image=happy)
    elif result > 20:
        emoji1Label.config(image=cool)
        emoji2Label.config(image=cool)


def reset_game():
    """Resets the game to the initial state for a new round."""
    global time_left, correct_words, wrong_words, i
    i = 0
    correct_words = 0
    wrong_words = 0
    time_left = 60  # Reset the timer to full
    wordEntry.config(state=NORMAL)
    counter.config(text='0')
    timerLabel.config(text='60')
    instruction.config(text="Type Word And Hit Enter")
    emoji1Label.config(image='')
    emoji2Label.config(image='')
    instruction.place(x=120, y=550)
    wordText.config(text=random.choice(word_list))  # Reset the word to a random choice from the list
    timer()  # Restart the timer


def play_game(event):
    """Handles the logic for each new word entered by the player."""
    global i, correct_words, wrong_words
    if wordEntry.get() != '':
        i += 1
        counter.config(text=i)
        instruction.config(text="")
        if time_left == 60 and i == 1:  # Checks if it's the start of the game
            timer()
        check_word()
        wordEntry.delete(0, END)  # Clears the input field after processing


def check_word():
    """Compares entered word with the displayed word and updates scores accordingly."""
    global correct_words, wrong_words
    if wordEntry.get() == wordText['text']:
        correct_words += 1
    else:
        wrong_words += 1
    wordText.config(text=random.choice(word_list))  # Update to a new random word


def slider():
    """Creates a moving text effect in the GUI."""
    global sliderwords, count
    text = 'Welcome to Speed Typing Test'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    movingText.config(text=sliderwords)
    count += 1
    movingText.after(100, slider)  # Recursive call to create a continuous moving effect


# Main GUI configuration
root = Tk()
root.title("Speed Typing Test")
root.iconbitmap('images/clock.ico')
root.geometry('800x680+610+130')
root.config(bg='pale turquoise')
root.resizable(0, 0)
# Load the logo image with a resized version (smaller)
logoImage = PhotoImage(file='images/logo.png').subsample(2, 2)  # Modify the subsample values to adjust size

# Place the logo in the center of the window
logo = Label(root, image=logoImage, bg='pale turquoise')
logo.place(x=(800 - logoImage.width()) // 2, y=110)  # Adjust the x-coordinate for central placement

movingText = Label(root, text='Welcome to Typing Speed Test', bg='pale turquoise', font=('arial', 25, 'bold italic'),
                   width=40, fg='#0f302e')
movingText.place(x=0, y=30)
slider()  # Initiate the slider effect
random.shuffle(word_list)
wordText = Label(root, text=word_list[0], font=('Courier New', 35, 'bold'), bg='pale turquoise')
wordText.place(x=397, y=420, anchor=CENTER)

countText = Label(root, text="WORDS", font=('Courier New', 28, 'bold'), bg='pale turquoise')
countText.place(x=60, y=140)

counter = Label(root, text="0", font=('Courier New', 28, 'bold'), bg='pale turquoise')
counter.place(x=90, y=200)

timeText = Label(root, text="TIME", font=('Courier New', 28, 'bold'), bg='pale turquoise')
timeText.place(x=630, y=140)

timerLabel = Label(root, text="60", font=('Courier New', 28, 'bold'), bg='pale turquoise')
timerLabel.place(x=650, y=200)

wordEntry = Entry(root, font=('Arial', 25, 'bold'), bd=9, justify=CENTER)
wordEntry.place(x=209, y=470)
wordEntry.focus_set()

instruction = Label(root, text="Type Word And Press Enter", font=('Courier New', 28, 'bold'), bg='pale turquoise',
                    fg='red')
instruction.place(x=120, y=550)
sad = PhotoImage(file='images/sad.png')
cool = PhotoImage(file='images/cool.png')
happy = PhotoImage(file='images/happy.png')
emoji1Label = Label(root, bg='pale turquoise')
emoji1Label.place(x=40, y=610)
emoji2Label = Label(root, bg='pale turquoise')
emoji2Label.place(x=680, y=610)

root.bind("<Return>", play_game)  # Bind the Enter key to the play_game function

root.mainloop()  # Start the GUI event loop
