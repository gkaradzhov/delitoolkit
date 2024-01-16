import os

import numpy as np
import torch
from delitoolkit.encoding_utils import SbertPredictor


class ProbingTargetPredictor(torch.nn.Module):
    def __init__(self, num_of_classes):
        super(ProbingTargetPredictor, self).__init__()
        self.pre_classifier = torch.nn.Linear(768, 512)
        self.dropout = torch.nn.Dropout(0.2)

        self.classifier = torch.nn.Linear(512, num_of_classes)

    def forward(self, vector_representation):
        pooler = self.pre_classifier(vector_representation)
        pooler = self.dropout(pooler)
        output = self.classifier(pooler)
        return output


class DeliAnnotationPredictor:
    def __init__(self, type_path='/models/predicting_type.zip',
                 probing_target_path='/models/predicting_probing_target_delidata20rc.zip',
                 nonprobing_target_path='/models/predicting_nonprobing_target_delidata20rc.zip') -> None:
        self.embedder = SbertPredictor('gtr-t5-xl')
        dir_path = os.path.dirname(os.path.realpath(__file__))

        device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

        self.type_model = ProbingTargetPredictor(num_of_classes=3)
        self.probing_target_model = ProbingTargetPredictor(num_of_classes=3)
        self.nonprobing_target_model = ProbingTargetPredictor(num_of_classes=4)

        self.type_model.load_state_dict(torch.load(dir_path + type_path, map_location=device))
        self.probing_target_model.load_state_dict(torch.load(dir_path + probing_target_path, map_location=device))
        self.nonprobing_target_model.load_state_dict(torch.load(dir_path + nonprobing_target_path, map_location=device))
        self.type_model.eval()
        self.probing_target_model.eval()
        self.nonprobing_target_model.eval()

        self.type_reverse_dict = {0: 'Probing', 1: 'Non-probing-deliberation', 2: '0'}
        self.probing_target_reverse_dict = {0: 'Moderation', 1: 'Reasoning', 2: 'Solution'}
        self.non_probing_reverse_dict = {0: 'Reasoning', 1: 'Solution', 2: 'Agree', 3: 'Disagree'}

    def predict(self, item):
        torch.random.manual_seed(42)
        encoded = torch.tensor(np.array(self.embedder.encode(item)))

        with torch.no_grad():
            type_prediction = self.type_reverse_dict[np.argmax(self.type_model.forward(encoded)).item()]
            if type_prediction == "0":
                return type_prediction, ''
            elif type_prediction == "Probing":
                target_predictio = self.probing_target_reverse_dict[
                    np.argmax(self.probing_target_model.forward(encoded)).item()]
            elif type_prediction == "Non-probing-deliberation":
                target_predictio = self.non_probing_reverse_dict[
                    np.argmax(self.nonprobing_target_model.forward(encoded)).item()]

            return type_prediction, target_predictio
