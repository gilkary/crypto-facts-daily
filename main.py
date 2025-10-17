import random

def load_facts(path="data/facts.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    facts = load_facts()
    fact = random.choice(facts)
    print("💡 Random Crypto Fact:")
    print(fact)

if __name__ == "__main__":
    main()
