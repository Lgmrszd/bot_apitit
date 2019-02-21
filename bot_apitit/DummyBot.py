from bot_apitit.Bot import Bot
from bot_apitit.Message import IncomingMessage
from bot_apitit.User import User


class DummyBot(Bot):
    platform = "dummy"

    def __init__(self, config: dict):
        super().__init__(config)
        self.user = User(1)

    def _auth(self):
        print("Dummy auth")

    def run(self):
        while True:
            print("User(ID:1): ", end="")
            user_text = input()
            message = IncomingMessage(user_text, self.user)
            if user_text == "!!exit":
                break
            self.catch(message)

    def send_to_user(self, user, message):
        if user.id == self.user.id:
            print("DummyBot: " + message.text)
