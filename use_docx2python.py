from docx2python import docx2python

# extract docx content
def get_text_by_docx2python(path):
    text = docx2python(path).text
    return text

