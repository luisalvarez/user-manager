from mongoengine import Document
from mongoengine.fields import StringField, URLField, DateTimeField

class User(Document):
    """
    App project mongo model
    """
    name = StringField(max_length=50, required=True)
    surname = StringField(max_length=50, required=True)
    birthdate = DateTimeField(null=True)
    zip_code = StringField(max_length=10)

    @property
    def created(self):
        return self.id.generation_time.isoformat() if self.id else None

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'surname': self.surname,
            'birthdate': self.birthdate,
            'zip_code': self.zip_code
        }
