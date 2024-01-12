import csv
import os


class DeliData:
    def __init__(self):
        files = os.listdir('delidata')
        self.corpus = {}
        for f in files:
            with open('delidata/' + f, 'r', encoding="utf8") as rf:
                a = [{k: v for k, v in row.items()} for row in
                     csv.DictReader(rf, delimiter='\t', skipinitialspace=True)]
                self.corpus[f] = a
