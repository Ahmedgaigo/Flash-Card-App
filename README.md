# Flash-Card-App
Flashy is a vocabulary flashcard App built using the Tkinter library in Python. It aims to help users learn French words by presenting them with interactive flashcards. The game provides a user-friendly interface where users can test their knowledge and track their progress.

Features:

1. Flashcard Presentation: The app displays French words(for trial) on the front side of the flashcard and their corresponding English translations on the back side. Users can flip the cards to reveal the English translations.

2. Randomized Vocabulary: The app uses a CSV file ("data/french_words.csv") to store a list of French words and their English translations. Each time a user interacts with a flashcard, a new word is randomly selected from the list.

3. Progress Tracking: The app keeps track of the user's progress by removing words from the list once they are correctly identified. The user's progress is saved in a separate CSV file ("data/words_to_learn.csv") to allow for continuous learning across multiple sessions.

4. User-Friendly Interface: The app features a clean and intuitive interface. Flashcards are displayed on a canvas, and buttons for "known" and "unknown" are provided to proceed to the next flashcard or mark the current word as learned.

To use Flashy, run the script and interact with the flashcards. Start by viewing the front side of the card, which displays a French word. Try to recall the English translation before flipping the card to check your answer. Click the "right" button if you knew the translation or the "wrong" button if you didn't. The game will track your progress and present new words accordingly.

Immerse yourself in vocabulary learning with Flashy and enhance your language skills one flashcard at a time!

