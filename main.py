def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    lowecase_contents = file_contents.lower()
    contents_list = lowecase_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print (f"{len(contents_list)} words found in the document\n")
    
    alphabet_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabet_list = alphabet_list.split()
    dictionary_count = {}
    for letter in alphabet_list:
        count = lowecase_contents.count(letter)
        dictionary_count[letter] = count
        print (f"The '{letter}' character was found {dictionary_count[letter]} times")
    
    # print(len(contents_list))    
    
main()
