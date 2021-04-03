import numpy as np
import editdistance 

def cleanup_labels(data):
    data.sort()
    filtered = []

    search_range = 2
    threshold = 8

    i = 0
    while i < len(data):
        lower = i - search_range
        upper = i + search_range
        try:
            for word in data[lower:upper]:
                add = False
                for word2 in data[lower:upper]:
                    if not word2 in filtered and editdistance.eval(word, word2) > threshold:
                        add = True      
                if add:
                    filtered.append(word)
        except Exception:
            continue
        i += search_range

    # remove duplicates
    final = []
    for i in filtered:
        if i not in final:
            final.append(i)

    return final