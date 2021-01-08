def cleanPunc(str):
    for char in '-.,\n':
        str = str.replace(char, ' ')
    str = str.lower()
    return str

def count(dictionary, elements):
    if elements in dictionary:
        dictionary[elements] += 1
    else:
        dictionary.update({elements: 1})
    return dictionary

if __name__ == "__main__":
    Sentence = "Apple, Apple Mango. Mango Orange Mango Guava Guava. Mango- Apple Mango Orange Mango Guava Guava Mango"
    list_of_words = cleanPunc(Sentence).split()
    dictionary = {}

    for elements in list_of_words:
        dictionary = count(dictionary, elements)

    print(dictionary)

