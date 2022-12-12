
def reverse_words(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) >= 5 and word[-1] in [".", "!", "?"]:
            new_words.append(word[:-1][::-1])
            new_words.append(word[-1])
        elif len(word) >= 5:
            new_words.append(word[::-1])
            new_words.append(" ")
        elif len(word) == 5:
            new_words.append(word.upper())
            new_words.append(" ")
        else:
            new_words.append(word)
            new_words.append(" ")

    new_words[0] = new_words[0].capitalize()
    if new_words[-1] not in [".", "!", "?"]:
        new_words[-1] = (".")

    return "".join(new_words)