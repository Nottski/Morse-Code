from morse_dictionary import MorseDictionary


class MorseInterpreter:
    def __init__(self):
        self.morse_message = "No new messages"
        self.dictionary = MorseDictionary()

    def welcome_message(self):
        return "Welcome to the Morse Code Encoder!"

    def interpret_text(self):
        user_text = input("What is your message? ").replace(" ", "").upper()
        if user_text == "REPEAT":
            return self.morse_message
        self.morse_message = ""
        for char in user_text:
            if char not in self.dictionary.dictionary:
                print("The symbol you entered is not in this programme's dictionary, please use the 26 letters of the "
                      "Latin Alphabet, Arabic numerals 0 to 9 or the symbols: . , ? ' ! / ( ) & : ; = + - @. Please "
                      "transliterate if possible")
                return self.interpret_text()
            else:
                self.morse_message += self.dictionary.dictionary[char] + "  "
        return self.morse_message

    def user_followup(self):
        user_followup = input("Do you have another message to encode? Y/N ").lower()
        if user_followup == "n":
            print("Have a nice day.")
            return False
        elif user_followup == "y":
            return True
        else:
            print("Please answer Y or N.")
            self.user_followup()
