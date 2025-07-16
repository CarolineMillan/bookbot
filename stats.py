def count_words(content):
    ## counts the number of words in the string 'content'
    words = content.split()
    num_words = len(words)
    return num_words

def count_chars(content):
    dict = {}
    for char in content:
        my_char = char.lower()
        if my_char in dict:
            dict[my_char] += 1
        else:
            dict[my_char] = 1
    return dict

def sort_on(items):
    return items["num"]

def sort_char_count(dict):
    sorted_chars = []
    for key in dict:
        sorted_chars.append({"char" : key, "num" : dict[key]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars