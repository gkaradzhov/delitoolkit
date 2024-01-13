import csv
import os


class DeliData:
    def __init__(self):
        files = os.listdir('delitoolkit/delitoolkit/delidata_corpus')
        self.corpus = {}
        for f in files:
            if f == '__init__.py':
                continue
            with open('delitoolkit/delitoolkit/delidata_corpus/' + f, 'r', encoding="utf8") as rf:
                a = [{k: v for k, v in row.items()} for row in
                     csv.DictReader(rf, delimiter='\t', skipinitialspace=True)]
                self.corpus[f] = a
