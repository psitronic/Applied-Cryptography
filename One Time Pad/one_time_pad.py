"""
An implementation of the one-time pad encryption technique.
"""
def encode_message(msg, key, nbits):
    """
    The function to encrypt a message
    Takes three arguments:
        string msg - a message to be encoded
        string key - a key with the length len(msg) * nbits. If key == None
                     the function finds a pseudorandom key
        integer nbits - number of bits for each symbol in the message
    Returns an encrypted message as a string
    """
    from random import randint
    msg_in_bits = message_to_bits(msg, nbits)
    
    if key == None:
        key = [randint(0,1) for i in range(len(msg_in_bits))]
    else:
        if len(key) < len(msg_in_bits):
            raise ValueError("The key should have the same size as, or longer than, the message.")
        else:
            key = list(map(int, key))
    
    encoded_msg = [msg_in_bits[i]^key[i] for i in range(len(msg_in_bits))]
    
    return {'msg':''.join(str(el) for el in encoded_msg), 'key':''.join(str(el) for el in key)}

def message_to_bits(msg, nbits):
    """
    Converts each letter in message to binary format with nbits length
    Takes msg as a string and nbits as an integer
    Returns a binary representation of the message as an array
    """
    msg_in_bits = []
    for char in msg:
        msg_in_bits += int_to_bits(char_to_int(char), nbits)

    return msg_in_bits.copy()

def int_to_bits(n, pad):
    """
    Converts the decimal char representation to the binary format
    Takes an integer number n - a decimal code of a letter; integer pad is a number of bits
    Returns an array
    """
    result = [0] * pad
    pos = pad - 1
    
    while n > 0:
        result[pos] = (0 if n % 2 == 0 else 1)

        n = n//2
        pos -= 1
        
    return result.copy()

def char_to_int(char):
    
    return ord(char)

      
def decode_msg(msg,key,nbits):
    """
    The function to decrypt the message
    Takes three arguments:
        string msg - a message to be decoded
        string key - a key with the length len(msg) * nbits. If key == None
                     the function finds a pseudorandom key
        integer nbits - number of bits for each symbol in the message
    Returns an decrypted message as a string
    """
    decoded_msg = ""
    msg_in_bits = [int(msg[i])^int(key[i]) for i in range(len(msg))]
    for n in range(len(msg_in_bits)//nbits):
        pad = msg_in_bits[n * 7: (n + 1) *7]
        char_code = bits_to_int(pad,nbits)
        decoded_msg += int_to_char(char_code)
    
    return decoded_msg

def bits_to_int(msg_in_bits, nbits):
    """
    The fucntion to conver a binary representation to decimal
    """
    loc = nbits - 1
    code = 0
    for bit in msg_in_bits:
        if bit == 1:
            code += 2**loc
        loc -= 1
    return code
        
def int_to_char(code):
    return chr(code)

enc_msg = encode_message(msg = 'AB', key = None, nbits = 7)
dec_msg = decode_msg(enc_msg['msg'],enc_msg['key'],7)
print(dec_msg)