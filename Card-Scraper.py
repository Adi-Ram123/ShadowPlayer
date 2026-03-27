import requests
import json
import csv
import re
import os

# Function to clean HTML-like tags from ability text
def clean(text):
    if text:
        return re.sub(r"<.*?>", "", text)
    return ""

# Fetch all cards from DotGG
url = "https://api.dotgg.gg/cgfw/getcards"
params = {"game": "shadowverse"}
response = requests.get(url, params=params)
cards = response.json()

print(f"Total cards fetched: {len(cards)}")

# Save CSV in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, "shadowverse_cards.csv")

print("CSV will be saved at:", csv_file)

# Decide which fields to include in CSV
fields = [
    "id",
    "name",
    "cost",
    "attack",
    "health",
    "ability",
    "evolved_ability",
    "class",
    "type",
    "tribes"
]

# Write CSV
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    for card in cards:
        # Replace type = 4 with 'spell'
        card_type = card.get("type")
        if card_type == '4':
            card_type = "Spell"

        row = {
            "id": card.get("id"),
            "name": card.get("name"),
            "cost": int(card.get("cost", 0)),
            "attack": int(card.get("atk", 0)),
            "health": int(card.get("life", 0)),
            "ability": clean(card.get("skill_text")),
            "evolved_ability": clean(card.get("evo_skill_text")),
            "class": card.get("color"),
            "type": card_type,
            "tribes": ",".join(card.get("tribes", [])),
        }
        writer.writerow(row)

print(f"CSV saved successfully!")