import os
import PyPDF2
import re


def extract_abstracts(path):
    with open(path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        document_text = ''

        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            document_text += page.extract_text()

    standard_abstract = re.compile(r'\bAbstract\b', re.IGNORECASE)
    abstract_start = standard_abstract.search(document_text)

    standard_keywords = re.compile(r'\bKeywords\b', re.IGNORECASE)
    keywords_start = standard_keywords.search(document_text)

    file_name = path.split('/')[-1].split('.')[0]

    if abstract_start and keywords_start:
        abstract = document_text[abstract_start.end(
        ):keywords_start.start()].strip()
        return f"{file_name} - Abstract:\n{abstract}"
    else:
        return None


def join_abstracts(dir_location, out_file):
    with open(out_file, 'w', encoding='utf-8') as final_file:
        for file_name in os.listdir(dir_location):
            if file_name.endswith('.pdf'):
                dir_path = os.path.join(dir_location, file_name)
                abstract = extract_abstracts(dir_path)

            if abstract:
                final_file.write(abstract + '\n\n')


dir = 'papers/2023'
output_file = 'abstracts2023.txt'

join_abstracts(dir, output_file)
