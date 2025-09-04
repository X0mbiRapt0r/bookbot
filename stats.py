def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(chars):
    return chars["num"]

def char_dict_to_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    return char_list