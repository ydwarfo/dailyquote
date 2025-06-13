import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't watch the clock; do what it does. Keep going."
]

def main():
    quote = random.choice(quotes)
    print("\n💡 Quote of the Day:\n")
    print(f"\"{quote}\"\n")

if __name__ == "__main__":
    main()