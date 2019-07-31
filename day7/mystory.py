story = """I'm a little teapot
I'm a little {0},
Short and stout,
Here is my {1}
Here is my spout
When I get all steamed up,
Hear me shout,
Tip me over and {2} me out!

I'm a very special {0},
Yes, it's true,
Here's an example of what I can do,
I can turn my {2} into a spout,
Tip me over and {2} me out!"""

noun = raw_input("Enter an noun: ")
verb = raw_input("Enter an verb: ")
someThingYouHold = raw_input("Enter an someThingYouHold: ")

#display the story using string interpol
print story.format(noun,verb,someThingYouHold)

