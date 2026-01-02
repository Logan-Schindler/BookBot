def get_num_words(text):
    return len(text.split())

def dict_letters(text):
    no_space_text = text.lower().replace(" ", "")
    letters = {}

    #Start loop
    for i in range(0,len(no_space_text)):
        if no_space_text[i] in letters:
            letters[no_space_text[i]] = letters[no_space_text[i]] + 1
        else:
            letters[no_space_text[i]] = 1
    
    return letters

def sort_on(items):
    return items["num"]

def sort_list_letters(text):
    dict_of_letters = dict_letters(text)
    list_of_letters = []
    for letter in dict_of_letters:
        if letter.isalpha():
            list_of_letters.append({"letter":letter, "num":dict_of_letters[letter]})
    list_of_letters.sort(reverse=True, key=sort_on)
    return list_of_letters

def create_output(text):
    sorted_char_count = sort_list_letters(text)
    output = ""
    for char in sorted_char_count:
        output += f"{char["letter"]}: {char["num"]}\n"
    return output








