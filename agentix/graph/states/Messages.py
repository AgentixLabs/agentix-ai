from enums import Models

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def __str__(self):
        return self.content

    def __call__(self, model: Models):
        if model == Models.OPENAI:
            return {
                "role": self.role,
                "content": [
                    {
                        "type": "text",
                        "text": self.content
                    }
                ]
            }

class HumanMessage(Message):
    def __init__(self, content):
        super().__init__("user", content)

class AssistantMessage(Message):
    def __init__(self, content):
        super().__init__("assistant", content)

class SystemMessage(Message):
    def __init__(self, content):
        super().__init__("system", content)
