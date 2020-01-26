import math
import re
from decimal import Decimal

def occurence(sentences, text):
    text = re.findall(r'[^.]+.', text.lower())
    if type(sentences) == list:
        multiple = True
        sentences = [i.lower() for i in sentences]
    else:
        sentences = [sentences.lower()]

    total = 0
    for j in text:

        temp = 0
        for sentence in sentences:
            if sentence in j:
                temp += 1
            if temp == len(sentences):
                total += 1
    return total


def compute(fx, fy, fxy, N):
    fx = log2(fx)
    fy = log2(fy)
    fxy = log2(fxy)
    return (max(fx, fy) - fxy) / (log2(N) - min(fx, fy))

def log2(x):
    if x == 0:
        return math.log2(0.1)
    return math.log2(x)

def similarity(term1, term2, source):
    fx = occurence(term1, source)
    fy = occurence(term2, source)
    fxy = occurence([term1, term2], source)
    N = sum([1 for i in re.findall(r'[^.]+.', source.lower())])
    print(N)
    return math.exp(-compute(fx, fy, fxy, N))


if __name__ == '__main__':
    with open('test.txt','r', encoding='utf-8') as f:
        x = similarity("related", "other", f.read())
    print(x)
