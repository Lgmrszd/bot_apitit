from abc import ABC, abstractmethod


__accept_modes = ("command", "all")


class Handler(object):
    default_command = ""

    def __init__(self, command_name, accept_mode="command"):
        self.command_name = command_name
        self.accept_mode = accept_mode

    @abstractmethod
    def execute(self, fixed_text, message, bot_instance):
        pass

