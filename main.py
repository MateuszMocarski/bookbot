def main():
    path_to_book = "books/frankenstein.txt"
    text = read_book(path_to_book)
    characters_dictionary = count_characters(text)
    list_of_characters_dictionaries = convert_dictionary_to_list(characters_dictionary)
    
    print(create_sorted_list(list_of_characters_dictionaries))


def read_book(path_to_book):
    with open(path_to_book) as f:    
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters

def convert_dictionary_to_list(dict):
    list_of_characters = []
    for key in dict:
        small_dict = {"letter" : key, "count" : dict[key]}
        list_of_characters.append(small_dict)
    return list_of_characters

def sort_on(dict):
    return dict["count"]

def create_sorted_list(dict):
    dict.sort(reverse = True, key = sort_on)
    return dict


main()