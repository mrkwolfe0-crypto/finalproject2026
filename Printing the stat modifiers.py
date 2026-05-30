import random
dice_roll = []
def roll():
    return random.randint(1,6)

def stat():
    dice_roll = []
    d1 = roll()
    dice_roll.append(d1)
    d2 = roll()
    dice_roll.append(d2)
    d3 = roll()
    dice_roll.append(d3)
    d4 = roll()
    dice_roll.append(d4)
    dice_roll.sort(reverse = True)
    total = sum(dice_roll[0:3])
    return total

def Player_stat():
    result = {}
    Players_stats = ["STR", "DEX", "CON",
                     "INT", "WIS", "CHA"]
    for Player_stat in Players_stats:
        pstat = stat()
        key = Player_stat
        value = pstat
        result[key] = value
    return result

def get_modifier(Player_stat):
    return (Player_stat - 10) // 2

pstats = Player_stat()
print(pstats)
print("\nModifier Scores\n")

for stat_name, score in pstats.items():
    mod = get_modifier(score)
    print(f"{stat_name}: {score}  Modifier: {mod}")
"""
That line will work, but as you guessed, it will have a "jagged" look because STR and CHA are different lengths, and 8 and 15 are different lengths.
To get those perfect columns without needing to guess how many spaces to type, you can use **field width specifiers** inside your f-string. This tells Python, "Reserve X amount of space for this value."
### How to use column padding
In an f-string, you add :X (where X is the number of spaces) after the variable name to reserve a fixed width.
 * {stat_name:<4}: This reserves 4 spaces for the stat name and aligns it to the left.
 * {score:<3}: This reserves 3 spaces for the score and aligns it to the left.
Here is how you would structure it to make everything line up vertically:
```python
# The header
print(f"{'Stat':<5} {'Score':<5} {'Modifier'}")

# The loop
for stat_name, score in pstats.items():
    mod = get_modifier(score)
    # The numbers inside the curly braces set the column width
    print(f"{stat_name:<5} {score:<5} {mod}")

```
### Why this is the "best" way:
 1. **Alignment**: Because you’ve set a width of 5, the "Score" column will always start at the exact same horizontal position, regardless of whether the stat is a single digit or a double digit.
 2. **No More Counting**: You don't have to manually count spaces or hit the spacebar multiple times. You just define the "lane" you want the data to live in.
 3. **Scalability**: If you ever decide to add a "Saving Throw" column later, you just add one more {value:<width} block to the print statement, and the whole table stays perfectly aligned.
Does using the :< syntax make sense as a way to create those "invisible containers" for your data, or does it feel like it’s adding too much extra complexity to your print statements?
To achieve static spacing in console output regardless of the length of the data, you are looking for a concept called **"String Formatting"** or **"Field Width Padding."** Here are the best resources to understand how this works:
### 1. The Official Python Documentation (f-strings)
This is the "source of truth." Look for the section on "Format Specification Mini-Language." It explains how you can add width and alignment directly into your f-strings to force text into fixed-size containers.
 * Python f-string format specification documentation
### 2. Explanation of "Padding and Alignment"
This tutorial explains the specific syntax (like :< and :>) used to control how a string is padded with spaces to fit a specific width. This is the exact mechanism that prevents your columns from shifting when you move from single-digit numbers to double-digit numbers.
 * Python String Alignment Tutorial
### 3. Conceptual Visualization
To understand *why* this works, it helps to think of it as allocating a "box" of a specific width. If the text is shorter than the box, the system automatically fills the remainder with spaces. If you are interested in the broader concept of tabular formatting, you can look into:
 * Fixed-width data formatting
### Key Concepts to look for in these links:
 * **Field Width:** The number you place after the colon in a format specifier, which tells Python exactly how many characters wide that "slot" should be.
 * **Alignment Operators:** These are the symbols (< for left, > for right, ^ for center) that tell Python where to place the text inside the width you’ve allocated.
 * **Padding:** The process of filling the remaining characters in that width with empty spaces automatically.
By mastering these three concepts, you move from "guessing spaces" to "structuring data," which is the fundamental difference between a messy console output and a clean, readable table.
"""
print(f"{'Stat':<5} {'Score':<5} {'Modifier'}")

