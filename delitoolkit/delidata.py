import csv
import os



class DeliData:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        files = os.listdir(dir_path + '/delidata_corpus/')

        self.corpus = {}
        for f in files:
            if f == '__init__.py' or f == "__pycache__":
                continue
            with open(dir_path + '/delidata_corpus/' + f, 'r', encoding="utf8") as rf:
                a = [{k: v for k, v in row.items()} for row in
                     csv.DictReader(rf, delimiter='\t', skipinitialspace=True)]
                self.corpus[f] = a
