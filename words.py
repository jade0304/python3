words = ["i", "love", "you", "emily"]

def print_upper_words(words):
    """For a list of words, print out each word on a separate line, 
    but in all uppercase

        print_upper_words(["i", "love", "you"])
        I
        LOVE
        YOU

    """
    for word in words:
        print(word.upper())


def print_upper_wordsE(words):
    """prints words that start with the letter ‘e’ or 'E '(either upper or lowercase)

    >>> print_upper_wordsE(words)
    EMILY
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word uppercased if starts with one of given letter, 

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
