# Importing spellchecker library
from spellchecker import SpellChecker

# Step-I --> Creating class for app
class SpellCheckerApp:
    # Step-II --> Creating dunder function to create object of spellChecker library 
    def __init__(self):
        self.spell = SpellChecker()
    
    # Step-III --> Creating function to convert wrong spelling into right 
    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word:  # Check if correction is needed
                print(f"Converting {word} to {corrected_word}")
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)  # Add the unchanged word
        
        # Step-IV --> Using join function to join the list of words into a full sentence
        return " ".join(corrected_words)

    def mainRun(self):
        print("\n------Spell Checker-------\n")

        while True:
            text = input("\nEnter the text (q for exit): ").strip()
            if text.lower() == "q":
                print("Closing the App.......\n")
                break

            corrected_text = self.correct_text(text)
            print(f"Corrected text = {corrected_text}")


# Step-V --> Creating an object for class to run the app

if __name__ == "__main__":
    app = SpellCheckerApp()  # Create an instance of the class
    app.mainRun()  # Call the method on the instance
