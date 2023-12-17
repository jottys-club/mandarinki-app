from repositories.ml import MLRepository


class MLService:
    def __init__(self, ml_respository: MLRepository):
        self._repository: MLRepository = ml_respository

    def create_log(self, **kwargs):
        return self._repository.add(**kwargs)

    def generate(self, **kwargs) -> (str, int):
        pass
