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
            raise NameError("The key should have the same size as, or longer than, the message.")
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
    pos = 0
    
    while n > 0:
        result[pos] = (0 if n % 2 == 0 else 1)

        n = n//2
        pos += 1
        
    return result.copy()

def char_to_int(char):
    
    return ord(char)

