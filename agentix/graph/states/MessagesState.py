from Messages import *
from enums import Models

class MessagesState:
    def __init__(self, model: Models, system_message: str=None):
        self.model = model
        if system_message:
            self.messages = [SystemMessage(system_message)]
            self.history = [self.messages[0](self.model)]
        else:
            self.messages = []
            self.history = []

    def append(self, message: Message):
        self.messages.append(message)
        self.history.append(message(self.model))

    def __call__(self):
        return self.history
