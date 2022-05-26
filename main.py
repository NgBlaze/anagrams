def find_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()

    if len(first_word) == len(second_word):

        sorted_first_word = sorted(first_word)
        sorted_second_word = sorted(second_word)

        if sorted_first_word == sorted_second_word:
            print("True")
        else:
            print("False")

    else:
        print("False")

