from abc import ABC, abstractmethod
from bot_apitit.Message import Message
from bot_apitit.Handlers import Handler


class Bot(ABC):
    platform = None

    # @abstractmethod
    def __init__(self, config: dict):
        self.__prefix = config.get("prefix") or "!"
        self.__handlers = {"command": [], "all": []}
        self._auth()

    @abstractmethod
    def _auth(self):
        pass

    @abstractmethod
    def send_to_user(self, user, message):
        pass

    def register_handler(self, handler: Handler):
        if handler.accept_mode == "command":
            self.__handlers["command"].append(handler)
        elif handler.accept_mode == "all":
            self.__handlers["all"].append(handler)

    def catch(self, message: Message):
        text = message.text
        if text.startswith(self.__prefix):
            text = text[len(self.__prefix):]
            for command_handler in self.__handlers["command"]:
                assert isinstance(command_handler, Handler)
                command_prefix = command_handler.command_name+" "
                if text.startswith(command_prefix):
                    command_handler.execute(text[len(command_prefix):], message, self)
                    return

        for command_handler in self.__handlers["all"]:
            assert isinstance(command_handler, Handler)
            command_handler.execute(text, message, self)

    @abstractmethod
    def run(self):
        pass

