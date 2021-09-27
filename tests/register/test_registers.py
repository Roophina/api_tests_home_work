from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse, RegisterUserResponseInvalid, RegisterUserInt


class TestRegisterUser:
    def test_register_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        #"""
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data_info.message == ResponseText.MESSAGE_REGISTER_USER

    def test_register_user_with_empty_username(self, app):
        """
        1. Try to register user with empty username
        2. Check that status code is 400
        3. Check response
        #"""
        data = RegisterUser.random()
        setattr(data, 'username', None)
        res = app.register.register(data=data, type_response=RegisterUserResponseInvalid)
        assert res.status_code == 400
        assert res.data_info.message == ResponseText.MESSAGE_REGISTER_USER_INVALID

    def test_register_user_with_empty_password(self, app):
        """
        1. Try to register user with empty password
        2. Check that status code is 400
        3. Check response
        #"""
        data = RegisterUser.random()
        setattr(data, 'password', None)
        res = app.register.register(data=data, type_response=RegisterUserResponseInvalid)
        assert res.status_code == 400
        assert res.data_info.message == ResponseText.MESSAGE_REGISTER_USER_INVALID

    def test_register_user_twice(self, app):
        """
        1. Try to register user with valid data
        2. Try to register user with valid data again
        2. Check that status code is 400
        3. Check response
        #"""
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data_info.message == ResponseText.MESSAGE_REGISTER_USER
        res2 = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res2.status_code == 400
        assert res2.data_info.message == ResponseText.MESSAGE_REGISTER_USER_TWICE

    def test_register_user_with_int_username(self, app):
        """
        1. Try to register user with int username
        2. Check that status code is 400
        3. Check response
        #"""
        data = RegisterUserInt.random()
        res = app.register.register(data=data, type_response=RegisterUserResponseInvalid)
        assert res.status_code == 400
        assert res.data_info.message == ResponseText.MESSAGE_REGISTER_USER_INVALID