from fixtures.auth.model import RegisterAuthResponse
from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse


class TestAuthUser:
    def test_auth_user_with_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        #"""
        data = RegisterUser.random()
        res_register = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res_register.status_code == 201
        assert res_register.data.message == ResponseText.MESSAGE_REGISTER_USER
        res_auth = app.auth.auth(data=data, type_response=RegisterAuthResponse)
        assert res_auth.status_code == 200
