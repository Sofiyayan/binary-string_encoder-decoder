def encoder(p_str):
    return "".join([format(ord(i), "08b") for i in p_str])


def decoder(b_str):
    return "".join([chr(int(b_str[i: i + 8], 2)) for i in range(0, len(b_str), 8)])
