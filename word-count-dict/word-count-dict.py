def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dict = {}

    for i in range(len(sentences)):
        print(i)
        print(f"dict sentence {i}")
        sentence = sentences[i]
        for j in range(len(sentence)):
            word = sentence[j]
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

    return dict