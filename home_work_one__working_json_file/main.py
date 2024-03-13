import json
# from pathlib import Path

# dir_ = Path('.')
# print([files for files in dir_.iterdir()])

def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    with open(file_path, 'r') as json_file_:
        json_file = json.load(json_file_)
        words_list = dict()
        for items in json_file['rss']['channel']['items']: # Выводим предложения из description
            for word in items['description'].split(): # Все слова из description по отдельности
                if len(word) > word_max_len:
                    if word not in words_list:
                        words_list[word] = 1
                    else:
                        words_list[word] += 1
    words_list_sorted = sorted(words_list.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
    top_words = [word[0] for word in words_list_sorted]
    return top_words


if __name__ == '__main__':
    print(read_json('newsafr.json'))