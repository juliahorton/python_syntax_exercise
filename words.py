def print_upper_words(words, must_start_with):
    """For a list of words, print out each word that begins with a specified letter on a separate line in all uppercase."""

    for word in words:
        if  word.startswith(must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "eh", "emmm"], ("h", "y"))