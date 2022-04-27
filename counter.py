import emoji


def parse_dataset(fp):
    '''
    Loads the dataset .txt file with label-tweet on each line and parses the dataset.
    :param fp: filepath of dataset
    :return:
        corpus: list of tweet strings of each tweet.
        y: list of labels
    '''
    y = []
    corpus = []
    with open(fp, 'rt', encoding="utf8") as data_in:
        for line in data_in:
            if not line.lower().startswith("tweet index"):  # discard first line if it contains metadata
                line = line.rstrip()  # remove trailing whitespace
                label = int(line.split("\t")[1])
                tweet = line.split("\t")[2]
                y.append(label)
                corpus.append(tweet)

    return corpus, y


def has_emoji(text):
    for char in text:
        if emoji.is_emoji(char):
            return True
    return False


c1, y1 = parse_dataset("dataset\\SemEval2018-T3-train-taskA_emoji.txt")
c2, y2 = parse_dataset("dataset\\SemEval2018-T3_gold_test_taskA_emoji.txt")

c_final = []
c_final.extend(c1)
c_final.extend(c2)

with_emoji = []
with_tag = []
with_link = []

for text in c_final:
    if has_emoji(text):
        with_emoji.append(text)

for text in c_final:
    if "@" in text:
        with_tag.append(text)

for text in c_final:
    if "http" in text:
        with_link.append(text)

print(len(c_final))
print(len(with_emoji))
print(len(with_tag))
print(len(with_link))
