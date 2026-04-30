print("Madlibs Game")


sample = """Bunnoo the rabbit planted a tiny seed ___ the garden. 
'Grow!' said Bunnoo. Nothing happened.
The next day: "Grow!" Nothing.
Every day, Bunnoo watered the seed and said hello ___ the soil.
One morning, a tiny green shoot appeared. It was so small!
"It's here!" shouted Bunnoo, jumping ___ joy.
The shoot grew and grew ___ a big, leafy plant. And it had little orange carrots underneath ___ the soil
"Good things come ___ those who wait," said Bunnoo's grandma.
Bunnoo smiled. He was glad he did not stop trying."""
print(sample)


prepositions = [
    "in",
    "on",
    "at",
    "under",
    "over",
    "with",
    "between",
    "among",
    "before",
    "after",
    "into",
    "underneath",
    "onto",
    "to",
]
 
print("clues", prepositions)
p1 = input("Enter first preposition : ")
p2 = input("Enter second preposition : ")
p3 = input("Enter third preposition : ")
p4 = input("Enter another preposition: ")
p5 = input("Enter another preposition: ")
p6 = input("Enter last preposition: ")

story = f"""Bunnoo the rabbit planted a tiny seed {p1} the garden. 
'Grow!' said Bunnoo. Nothing happened.
The next day: "Grow!" Nothing.
Every day, Bunnoo watered the seed and said hello {p2} the soil.
One morning, a tiny green shoot appeared. It was so small!
"It's here!" shouted Bunnoo, jumping {p3} joy.
The shoot grew and grew {p4} a big, leafy plant. And it had little orange carrots underneath {p5} the soil
"Good things come {p6} those who wait," said Bunnoo's grandma.
Bunnoo smiled. He was glad he did not stop trying."""

print("*" * 15,"THE FINAL STORY", "*" * 15)
print(story)

print("*" * 15,"THE END", "*" * 15)


