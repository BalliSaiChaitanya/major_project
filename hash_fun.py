def encrypt(msg, key='%txs'):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 256))
    return ''.join(encryped)

def decrypt(encryped, key='%txs'):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 256))
    return ''.join(msg)

"""if __name__ == '__main__':
    key = '%txsZYNgX8@eS+y#'
    msg = 'name'
    encrypted = encrypt(msg)
    decrypted = decrypt(encrypted)

    print ('Message:', repr(msg))
    print ('Key:', repr(key))
    print ('Encrypted:', repr(encrypted))
    print ('Decrypted:', repr(decrypted))"""