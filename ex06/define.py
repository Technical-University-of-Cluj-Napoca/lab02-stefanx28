import sys
import urllib.request
from html.parser import HTMLParser

class DefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_def = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            attrs = dict(attrs)
            if attrs.get('class', '') == 'def-wrapper':
                self.in_def = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_def:
            self.in_def = False

    def handle_data(self, data):
        if self.in_def:
            self.text.append(data)

def get_definition(word):
    url = f"https://dexonline.ro/definitie/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
    except:
        return "Word not found or error."
    parser = DefParser()
    parser.feed(html)
    text = ' '.join(parser.text).strip()
    if not text:
        return "Definition not found."
    lines = [line.strip() for line in text.split('. ') if line.strip()]
    return '. '.join(lines) + '.' if lines else "No definition."

def main():
    if len(sys.argv) != 2:
        print("Usage: python define.py <word>")
        sys.exit(1)
    word = sys.argv[1].strip()
    print(get_definition(word))

if __name__ == "__main__":
    main()