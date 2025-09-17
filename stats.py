def get_number_words(text):
    return len(text.split())

def get_num_each_letter(text):
    letter_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def sort_char_by_count(item):
    return item["count"]

def organize_dict(dict):
    letter_list = []
    for char in dict:
        letter_list.append({"char": char, "count": dict[char]})
    letter_list.sort(reverse=True, key = sort_char_by_count)
    return letter_list