import random


def read_text():
    with open("prince_book.txt", "r") as file:
        return file.readlines()


def clear_text(text):
    formatted_lines = []
    for line in text:
        stripped_line = line.strip()  # Видаляємо пробіли на початку і в кінці рядка
        if stripped_line:  # Перевірка, чи рядок не порожній після видалення пробілів
            lowercased_line = stripped_line.lower()  # Перетворює рядок на нижній регістр
            formatted_lines.append(lowercased_line)  # Додає відформатований рядок до списку

    result = ' '.join(formatted_lines)  # Об'єднуємо всі рядки в один рядок, розділені пробілом
    return result


def tokenize(text):
    for char in text:
        if char in ["!", "?", "'", ".", ",", ":", ";", "”", "“"]:
            text = text.replace(char, '')  # замінюємо символ на порожній
    return text.split()


def create_dictionary(tokens):
    word_dictionary = {}
    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i + 1]
        if current_word not in word_dictionary:
            word_dictionary[current_word] = [next_word]
        else:
            word_dictionary[current_word].append(next_word)
    return word_dictionary


def markov_chain(word_dictionary):
    first_word = random.choice(list(word_dictionary.keys()))
    generated_text = [first_word.capitalize()]
    for i in range(199):
        next_words = word_dictionary[first_word]
        first_word = random.choice(next_words)
        generated_text.append(first_word)
    return ' '.join(generated_text)


def main():
    text = read_text()
    cleared_text = clear_text(text)
    tokenized = tokenize(cleared_text)
    word_dictionary = create_dictionary(tokenized)
    print(markov_chain(word_dictionary))


main()
