def word_count(novel_string):
    num_words = len(novel_string.split())
    return num_words

def character_count(novel):
    
    character_count = {}
    novel_words = novel.split()
    for word in novel_words:
        word_char = word.split()
        for char in word:
            char = char.lower()
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1    

    return character_count

def sort_on(unsorted_list):
    return unsorted_list["num"]


def letter_sort(character_dict):

    sorted_list = []

    for char in character_dict:
        sorted_list.append({"char": char,"num": character_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    
    
    #print(f"the sorted list {sorted_list}")

    return sorted_list
