class KNN_classifier:
    def __init__(self, k: int):
        self.k = k

    def train(self, training_data, training_labels):
        self.training_data = training_data
        self.training_labels = training_labels