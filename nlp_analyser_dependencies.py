import spacy
from dataclasses import dataclass

nlp = spacy.load("pt_core_news_sm")

@dataclass
class Reports:
    category: str
    text: str
    reply: str
    abstract: list
    reply_abstract: list                                                       
    def parse_deps(self, doc, dependencies):
        for token in doc:
            dependencies.append((token.pos_, token.dep_, token.head.pos_, [child.pos_ for child in token.children]))

    def parse_abstracts(self):
        self.parse_deps(self.text, self.abstract)
        self.parse_deps(self.reply, self.reply_abstract)

category = "índice referencial não especificado"

text = nlp("Eu gosto de comer pizza com meus amigos")
reply = nlp("De que maneira você se sente mais satisfeito quando você vai comer pizza com os seus amigos?")

report = Reports(category=category, text=text, reply=reply, abstract=[], reply_abstract=[])
report.parse_abstracts()

print("Frase original: " + str(report.text))

print("Dependências sintáticas:")
for i in report.abstract:
    print(i)

print("resposta: " + str(report.reply))

for i in report.reply_abstract:
    print(i)
