def validation_encoder(p_str):
    if p_str.isascii():
        return True
    else:
        return False


def validation_decoder(b_str):
    for i in b_str:
        if int(i) == 0 or int(i) == 1:
            pass
        else:
            return (
                False,
                "Error: {} is invalid binary form. \n The binary form should contain only 0s and 1s.".format(
                    b_str
                ),
            )
    if len(b_str) % 8 == 0:
        pass
    else:
        return (
            False,
            "Error: {} has invalid length. \n The length of the input has to be multiple of 8.".format(
                b_str
            ),
        )
    return True, "Input is Valid"
