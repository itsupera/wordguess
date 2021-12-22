import json
import random
from collections import Counter


def main():
    cnt = Counter()
    for i in range(1, 30):
        with open("innocent_corpus/term_meta_bank_%d.json" % i) as f:
            for line in f:
                for d in eval(line):
                    cnt[d[0]] = d[2]

    frequent_words = {word for word, freq in cnt.most_common(5_000)}

    word_to_def = {}
    word_to_entry = {}
    for i in range(1, 24):
        with open("大辞泉/term_bank_%d.json" % i) as f:
            j = json.load(f)
            for elem in j:
                word = elem[0]
                if word in frequent_words:
                    definitions = elem[5][0]
                    first_definition = parse_definitions(definitions)
                    if first_definition:
                        word_to_def[word] = first_definition
                        word_to_entry[word] = elem

    words = list(word_to_def.keys())
    print(f"{len(words)} words selected")
    print("----------------------------------------\n")

    while True:
        word = random.choice(words)
        definition = word_to_def[word]
        print(f"Def: {definition}\n")
        input("[ Press Enter to reveal answer ]\n")
        print(f"Answer: {word} ({word_to_entry[word][1]})\n")
        #print(f"DEBUG: {word_to_entry[word]}\n")
        print("-----------------------------------------------\n")


def parse_definitions(definitions):
    if "㊀" in definitions:
        definitions = definitions.split("㊀")[1].split("㊁")[0]
    if "①" in definitions:
        first_definition = definitions.split("①")[1].split("②")[0]
        if first_definition:
            return first_definition
    return None


if __name__ == '__main__':
    main()
