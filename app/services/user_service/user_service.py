from app.models.user import User


class UserService(object):
    """
    Service for creating a new app project
    """
    @staticmethod
    def create_user(name, surname, birthdate, zip_code):
        """
        Create a new user
        """
        user = User(name=name, surname=surname, birthdate=birthdate, zip_code=zip_code).save()
        return user

    @staticmethod
    def list_users():
        """
        Get created projects
        :return:
        :rtype:
        """
        return User.objects()

    @staticmethod
    def get(user_id):
        """
        Get the user
        """
        User.objects(id=user_id)

    @staticmethod
    def delete_user(user_id):
        """
        Delete the user
        """
        User.objects(id=user_id).delete()

