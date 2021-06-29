class CaeserCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, message):
        return self._transform(message, self._backward)

    def _transform(self, message, code):
        message = message.upper()
        msg = list(message)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaeserCipher(3)
    message = "HELLO SIR!! PRANAV IS ON THE GATE"
    coded = cipher.encrypt(message)
    print(f"Secret: {coded}")
    decoded = cipher.decrypt('KHOOR VLU!! SUDQDY LV RQ WKH JDWH')
    print(f"Decoded: {decoded}")
