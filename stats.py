def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    import string

    lower_text = text.lower()
    # initialize dictionary for all lowercase letters a-z with 0
    counts = {ch: 0 for ch in string.ascii_lowercase}

    # count only lowercase alphabetic characters
    for ch in lower_text:
        if ch in counts:
            counts[ch] += 1

    return counts
