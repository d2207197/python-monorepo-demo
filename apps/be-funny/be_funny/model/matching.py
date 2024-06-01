import modeling

def train_matching_model(dataset: str = None):
    print(f"running {train_matching_model.__name__} with dataset {dataset}")
    data = dataset
    return modeling.train(data=data)
