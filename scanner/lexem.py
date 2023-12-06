class Lexem:
    def __init__(self, token, value=None) -> None:
        self.token = token
        self.value = value

    def __str__(self):
        return f"{self.token}({self.value})"
