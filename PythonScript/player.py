from langchain_core.language_models.base import BaseLanguageModel

class Player:
    def __init__(self, 
                 id: int,
                 name: str,
                 profile: str,
                 llm: BaseLanguageModel,
                 prompt_template: str):
        self.id = id
        self.name = name
        self.profile = profile
        self.llm = llm
        self.prompt_template = prompt_template 