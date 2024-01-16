import os
import pickle


class BoWSimple:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(dir_path + '/../models/bow_full_delidata.model', 'rb') as f:
            self.model = pickle.load(f)

    def predict_proba(self, dialogue_context):
        extended_context = ['BEGIN', *dialogue_context]
        bigrams = [p + "<SEP>" + n for p, n in zip(extended_context[:-1], extended_context[1:])]
        predictions = self.model.predict_proba(bigrams)

        return list(zip(dialogue_context, [p[1] for p in predictions]))
