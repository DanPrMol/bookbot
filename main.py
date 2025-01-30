def main():
    with open("/home/danielpmol/workspace/github.com/DanPrMol/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(file):
    return len(file.split())

def count_characters(file):
    lower_file = file.lower()
    char_count = {}
    for char in lower_file:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def dict_to_list(dict):
    return [{"chave": k, "valor": v} for k, v in dict.items()]

def sort_list(list):
    return list["valor"]

def report(file):
    print("--- Begin report of books/frankestein.txt ---")
    print(count_words(file), "words found in the document\n")
    dict = count_characters(file)
    list = dict_to_list(dict)
    list.sort(reverse=True, key=sort_list)
    for item in list:
        if item["chave"].isalpha():
            print("The", item["chave"], "character was found", item["valor"], "times")
    print("--- End of report ---")