import random
import string

greetings = [
    "🌸 Hello, I'm Saumya — your AI poetry companion!",
    "🖋️ Welcome! Saumya is here to help you weave words into wonder.",
    "💫 Ready to create magic? Saumya’s got your back!",
    "🎨 Hey there, poet! Let’s paint with words — together."
]

print(random.choice(greetings))
print("✨ I'll help you write a poem, one beautiful line at a time.\n")

# Themes with starter lines
themes = {
    "Love": [
        "Love is the fire that warms the soul.",
        "A whisper in the winds of time."
    ],
    "Nature": [
        "The forest breathes beneath the sky.",
        "The ocean sings its mighty song."
    ],
    "Hope": [
        "When darkness falls, still hope remains.",
        "A gentle voice in storms of doubt."
    ],
    "Loneliness": [
        "The room is filled with silent air.",
        "My thoughts echo against the wall."
    ],
    "Dreams": [
        "In dreams I fly where I belong.",
        "The stars become my stepping stones."
    ]
}

# Rhyme groups: words that rhyme together
rhyme_groups = {
    "time_group": ["time", "rhyme", "prime", "climb", "chime"],
    "soul_group": ["soul", "goal", "hole", "role", "whole"],
    "sky_group": ["sky", "high", "fly", "cry", "lie"],
    "song_group": ["song", "long", "strong", "wrong", "belong"],
    "remains_group": ["remains", "chains", "gains", "lanes", "rains"],
    "doubt_group": ["doubt", "shout", "about", "out", "route"],
    "air_group": ["air", "care", "share", "bare", "flare"],
    "wall_group": ["wall", "call", "fall", "small", "hall"],
}

def get_last_word(line):
    line = line.strip().lower()
    for p in string.punctuation:
        line = line.replace(p, '')
    words = line.split()
    return words[-1] if words else ""

def find_rhyme_group(word):
    for group, words in rhyme_groups.items():
        if word in words:
            return group
    return None

# --- Theme Selection ---
print("🎭 Available themes:", ", ".join(themes.keys()))
theme_input = input("🎨 Pick a theme or press Enter for random: ").title().strip()

if theme_input in themes:
    theme = theme_input
else:
    theme = random.choice(list(themes.keys()))
    print(f"🎲 Random theme chosen: {theme}")

# Starting line and rhyme
starting_line = random.choice(themes[theme])
start_word = get_last_word(starting_line)
current_group = find_rhyme_group(start_word)

print(f"\n🖋️ Starting line: {starting_line}")
if current_group:
    print(f"🎵 Rhyme group: {current_group}")
    rhymes = [w for w in rhyme_groups[current_group] if w != start_word]
    if rhymes:
        print(f"💡 Try to rhyme with: {random.choice(rhymes)}")
else:
    print("⚠️ No rhyme group found for the starting line.")

# Store poem lines
poem_lines = [starting_line]

# --- Line Writing Loop ---
while True:
    user_line = input("\n✏️ Write your next line (or type 'end' to finish): ").strip()
    if not user_line:
        print("⚠️ Please enter a valid line.")
        continue
    if user_line.lower() == "end":
        break

    poem_lines.append(user_line)
    user_word = get_last_word(user_line)
    user_group = find_rhyme_group(user_word)

    if user_group == current_group:
        print("✅ Nice! Your line rhymes well.")
        suggestions = [w for w in rhyme_groups[current_group] if w != user_word]
        if suggestions:
            print(f"💡 Other rhymes: {', '.join(suggestions)}")
    else:
        print(f"⚠️ '{user_word}' doesn't match the rhyme group.")
        if current_group:
            print(f"💡 Try rhyming with: {', '.join(rhyme_groups[current_group])}")

# --- Poem Output ---
print("\n📜 Your poem:\n")
for line in poem_lines:
    print(line)

# --- Optional Save ---
save = input("\n💾 Do you want to save this poem to a file? (yes/no): ").strip().lower()
if save == "yes":
    filename = input("📝 Enter file name (without extension): ").strip()
    with open(f"{filename}.txt", "w") as f:
        for line in poem_lines:
            f.write(line + "\n")
    print(f"✅ Poem saved as '{filename}.txt'")
else:
    print("🧾 Poem not saved.")
