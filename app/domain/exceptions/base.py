class DomainException(Exception):
    """Base domain exception."""
    pass

class EntityNotFoundException(DomainException):
    def __init__(self, entity_name: str, entity_id: str):
        super().__init__(f"{entity_name} with id '{entity_id}' not found.")
