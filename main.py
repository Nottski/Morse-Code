from morse_dictionary import MorseDictionary
from interpreter import MorseInterpreter

# Object-Oriented Approach
morse_dict = MorseDictionary()
morse_interp = MorseInterpreter()

encoder_on = True

while encoder_on:
    print(morse_interp.welcome_message())
    encoded_text = morse_interp.interpret_text()
    print(encoded_text)
    encoder_on = morse_interp.user_followup()


# Procedural Approach
# while encoder_on:
    # print("Welcome to the Morse Code Encoder!")
    # user_text = input("What is your message? ").replace(" ", "").upper()
    # morse_response = ""
    # for char in user_text:
    #     morse_response += morse_dict.dictionary[char] + "  "

    # print(morse_response)
    # user_followup = input("Do you have another message to encode? Y/N ").lower()
    # if user_followup == "n":
    #     encoder_on = False
    # elif user_followup == "y":
    #     pass
    # else:
    #     print("Please answer Y or N.")
    #     user_followup = input("Do you have another message to encode? Y/N ").lower()
    #     if user_followup == "n":
    #         encoder_on = False
    #     elif user_followup == "y":
    #         pass
