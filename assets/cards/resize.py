import os

no = ["tabletop.png", "back.png"]

"""
for i in os.listdir():
    if i not in no:
        os.system(f"convert {i} -resize 80x111\> {i}")
"""

image = "s05.png"
os.system(f"convert {image} -resize 80x111\> {image}")