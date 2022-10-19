import easygui
import re
from collections import Counter

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    text=text.lower()
    
    re.sub(r"[^a-zA-Z0-9]", '', text)
    words=re.split('[^a-zA-Z]', text)
    
    counter=Counter(words)
    counts=dict(counter)
    del counts['']   

    return counts


def test_run(path):
    with open(path, "r", encoding='UTF-8') as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))

    f.close()

path=easygui.fileopenbox()
test_run(path)

