from docx import Document
import os 

def process_doc_file(file_path) -> list:
    doc= Document(file_path)
    res = []
    # Получаем текст всех абзацев в документе
    # количество абзацев в документе
    for i in range(len(doc.paragraphs)):
        res.append(doc.paragraphs[i].text)
    return res
