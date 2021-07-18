# StoryModule

A module for creating `stories` which are represented as a collection of functions which point to each other, depending on the situation

# Usage

### Creating a new story
```py
from StoryModule import Story

class ExampleStory(Story): pass
```

### Now you can add storylines to it with the `@____.AddStoryLine()` decorator 
```py
@ExampleStory.AddStoryLine(name="start")
def starting(story_object : ExampleStory):
    #...
```

### The story object is passed in as a parameter so you can change the state of it
```py
@ExampleStory.AddStoryLine(name="start")
def starting(story_object : ExampleStory):
    story_object.at = "end" # this sets the current 'position' to be at the end storyline
```
### the return type is what will be returned when you run `.Advance()` later on...
```py
@ExampleStory.AddStoryLine(name="start")
def starting(story_object : ExampleStory):
    story_object.at = "end" # this sets the current 'position' to be at the end storyline
    return "you began a story"
```

### Once you are done adding storylines, you can now create as many story instances as you want
```py

StoryInstance1 = ExampleStory(at='start')
print( StoryInstance1.Advance() ) # "you began a story"
print( StoryInstance1.Advance() ) # "Story ended"

StoryInstance2 = ExampleStory(at='start')
print( StoryInstance2.Advance() ) # "you began a story"
print( StoryInstance2.Advance() ) # "Story ended"
```

### should you require additional state variables, you can override the constructor

```py
class ExampleStory(Story): 
    def __init__(self, at: str, PlayerName : str) -> None:
        super().__init__(at=at)
        self.PlayerName = PlayerName

@ExampleStory.AddStoryLine(name="SomeRandomStoryLine")
def Random(story_object : ExampleStory):
    # ...
    return f"Hello {story_object.PlayerName} !"
```

# Example

```py
from StoryModule import Story

class ExampleStory(Story): pass

@ExampleStory.AddStoryLine(name="start")
def starting(story_object : ExampleStory):
    story_object.at = "end" # this sets the current 'position' to be at the end storyline
    return "you began a story"

@ExampleStory.AddStoryLine(name="end") # name="end" is used before with ' story_object.at = "end" '
def starting(story_object : ExampleStory):
    story_object.end = True
    return "Story ended"

# you can now have as many story instances as you want

StoryInstance1 = ExampleStory(at='start')
print( StoryInstance1.Advance() ) # "you began a story"
print( StoryInstance1.Advance() ) # "Story ended"

StoryInstance2 = ExampleStory(at='start')
print( StoryInstance2.Advance() ) # "you began a story"
print( StoryInstance2.Advance() ) # "Story ended"

```
