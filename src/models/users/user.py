import uuid
import src.models.users.errors as UserErrors
from src.common.database import Database
from src.common.utils import Utils

__author__ = 'jushitaa'


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """

        This method verifies that an e-mail/password combo(as sent by the site form) is valid or not
        Check that email exists, and that the password associated to that email is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """

        user_data = Database.find_one("users", {"email": email}) # Password in sha512 -> pbkdf2_sha512
        if user_data is None: #Tell user that their email doesn't exist
            raise UserErrors.UserNotExistsError("Your user doesn't exist")

        if not Utils.check_hashed_password(password, user_data['password']): # Tell user their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password is wrong")

