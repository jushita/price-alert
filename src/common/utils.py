from passlib.hash import pbkdf2_sha512


__author__ = 'jushitaa'


class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the Login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):

        """
        Checks if the password user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage.
        :param password:
        :param hashed_password:pbkdf2_sha512 encrypted password
        :return: True is password match False otherwise
        """

        return pbkdf2_sha512.verify(password, hashed_password)