from fixtures.user_info.api import UserInfo
from fixtures.user_info.model import AddUserInfo


class TestUserInfo:
    def test_add_user_info(self, app, register_auth):
        """
                1. Try to register user with int username
                2. Check that status code is 400
                3. Check response
                #"""
        data = AddUserInfo.random()
        res_add = app.user_info.add_user_info(uuid=register_auth.uuid, data=data, header=register_auth.header, type_response=None)
        assert res_add.status_code == 200
