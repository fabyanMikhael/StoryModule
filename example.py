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
