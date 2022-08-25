import textract

def get_word_text(path):
    text = textract.process("data/WP200 Topic 2 Study Guide Spring Term 2022-23-incomplete.docx")
    return text

print(get_word_text("data/WP200 Topic 2 Study Guide Spring Term 2022-23-incomplete.docx"))