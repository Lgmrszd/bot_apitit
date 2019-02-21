from botapitit.User import User
from botapitit.Chat import Chat


class Message(object):
    def __init__(self, text):
        self.text = text


class IncomingMessage(Message):
    def __init__(self, text, from_user: User):
        super().__init__(text)
        self.from_user = from_user


class IncomingChatMessage(IncomingMessage):
    def __init__(self, text, from_user: User, from_chat: Chat):
        super(IncomingChatMessage, self).__init__(text, from_user)
        self.from_chat = from_chat

