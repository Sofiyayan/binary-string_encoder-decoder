
import sys
from encoder_decoder import encoder
from encoder_decoder import decoder
from validator import validation_encoder
from validator import validation_decoder


def driver_function(user_choice):
    if user_choice.rstrip() == "1":
        user_input_encode = input("Please, input the line for encoder: ")
        if validation_encoder(user_input_encode):
            return encoder(user_input_encode)
        else:
            return (
                "Error: {} contains unsupported characters.\n The entered string should contain only latin "
                "letters, numbers and other characters.".format(user_input_encode)
            )
    elif user_choice.rstrip() == "2":
        user_input_decode = input("Please, input the line for decoder: ")
        if validation_decoder(user_input_decode)[0]:
            return decoder(user_input_decode)
        else:
            return validation_decoder(user_input_decode)[1]
    elif user_choice.rstrip() == "0":
        sys.exit()
    else:
        return "{} is not from the menu list.\n Please choose 1, 2 or 0.".format(
            user_choice
        )


user_choice = input(
    "Please, press 1 if you want to use encode function. \n"
    "Please, press 2 if you want to use decode function. \n"
    "Please, press 0 to exit.\n"
)

print(driver_function(user_choice))
