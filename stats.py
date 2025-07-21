DEFAULT_PATH = "books/frankenstein.txt"

def get_book_text(filepath=DEFAULT_PATH):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def sort_on(items_dict):
    return items_dict["count"]

def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def get_character_count(text):
    # Create a dictionary.
    # keys are every unique character in the text
    # value is the number of times the key character appears in the text.
    # all letters converted to lower case
    normalized_text = text.lower()
    character_counts = {}
    for character in normalized_text:
        if character in character_counts:
            character_counts[character]+=1
        else:
            character_counts[character] = 1
    return character_counts

def convert_dict_to_list(dict_input):
    list_output = []
    for key, value in dict_input.items():
        list_output.append({"char": key, "count": value})
    return list_output
        
        
def get_sorted_character_count(text):
    character_count_dict = get_character_count(text)
    character_count_list = convert_dict_to_list(character_count_dict)
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list
    
def generate_report(filepath="books/frankenstein.txt"):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    character_counts = get_sorted_character_count(text)
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += f"--------- Character Count -------\n"
    for entry in character_counts:
        report += f"{entry.get('char')}: {entry.get('count')}\n"
    report += f"============= END ==============="
    return report
