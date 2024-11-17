import random


start = "Reiz kādā tālā zemē"
story = [start]

story_parts = [
    "Kāds mazs zēns devās slīpēt.",
    "Bembis nopļāva pus mežu.",
    "Cilvēki dzīvoja mierā un harmonijā."
]

for _ in range(1):
    next_part = random.choice(story_parts)
    story_parts.remove(next_part)  
    story.append(next_part)

print(" ".join(story))
