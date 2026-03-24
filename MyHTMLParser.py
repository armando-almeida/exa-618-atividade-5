from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = [] 
        self.title = ""
        self.in_title = False 

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for k, v in attrs:
                if k == "src":
                    self.images.append(v) 
                    
        elif tag == "title":
            self.in_title = True 
            self.title = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False 
    def handle_data(self, data):
        if self.in_title:
            self.title += data