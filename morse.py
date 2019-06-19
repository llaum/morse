# pylint: disable=missing-docstring

MORSE_MAP = {"/":" ", ".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", \
            "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K", \
            ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", \
            ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", \
            "-..-":"X", "-.--":"Y", "--..":"Z"}

class Morse:
    def decode(self, message):
        if message == "":
            return ""

        phrase = []
        for letter in message.split(" "):
            phrase.append(MORSE_MAP[letter])
        return "".join(phrase)
