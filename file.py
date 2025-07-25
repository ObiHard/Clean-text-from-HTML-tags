import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text_without_tags = re.sub(r'<[^>]+>', '', html)
    lines = text_without_tags.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = '\n'.join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as out_file:
        out_file.write(cleaned_text)
delete_html_tags('draft.html')