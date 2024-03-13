import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    root = ET.parse('newsafr.xml').getroot()
    items = root.findall('channel/item')
    words_list = {}
    for description in items:
        for word in description.find('description').text.split(): # Все слова из description по отдельности
                if len(word) > word_max_len:
                    if word not in words_list:
                        words_list[word] = 1
                    else:
                        words_list[word] += 1
    words_list_sorted = sorted(words_list.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
    top_words = [word[0] for word in words_list_sorted]
    return top_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))