print("^^^" * 10)

print("        " "MADLIBS GAME ")

print("^^^" * 10)

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



user_inputs = []

for i in range(6):
    while True:
        p = input(f"Enter a preposistion {i+1} :").strip().lower()
        if p in prepositions:
            user_inputs.append(p)
            print(user_inputs)
            break
        else:
            print("Enter from the list")


story = """Bunnoo the rabbit planted a tiny seed {} the garden. 
'Grow!' said Bunnoo. Nothing happened.
The next day: "Grow!" Nothing.
Every day, Bunnoo watered the seed and said hello {} the soil.
One morning, a tiny green shoot appeared. It was so small!
"It's here!" shouted Bunnoo, jumping {} joy.
The shoot grew and grew {} a big, leafy plant. And it had little orange carrots underneath {} the soil
"Good things come {} those who wait," said Bunnoo's grandma.
Bunnoo smiled. He was glad he did not stop trying.""".format(*user_inputs)

print("*" * 15, "THE FINAL STORY", "*" * 15)
print(story)

print("*" * 15, "THE END", "*" * 15)
