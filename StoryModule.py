from __future__ import annotations
from typing import Union

class Story:
    STORY_LINE : dict[str,function] = {}
    def __init__(self, at : str = None, end : bool = False) -> None:
        self.at = at
        self.end = end

    def Advance(self) -> Union[None,str]:
        if self.end or self.at == None:
            return None
        result = self.STORY_LINE[self.at](self)
        return result
    
    @classmethod
    def AddStoryLine(cls, name : str):
        def decorator(func):
            cls.STORY_LINE[name] = func
        return decorator