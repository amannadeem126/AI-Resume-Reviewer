def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def get_filename(uploaded_file):
    return uploaded_file.name