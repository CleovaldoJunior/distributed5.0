from Crypto import Random
from Crypto.PublicKey import ElGamal

def encryptionKey(bits):
    return ElGamal.generate(bits, Random.new().read)
