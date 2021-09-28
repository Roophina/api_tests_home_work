from fixtures.auth.model import AuthorizationRequiredResponse
from fixtures.user_info.model import UpdateUserInfo, UpdateUserResponse


class TestPutUserInfo:
    def test_update_user_info_with_valid_data(self, app, register_auth_info):
        """
        1. Update user info with valid data
        2. Check that status code is 200
        """
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=register_auth_info.header,
            type_response=UpdateUserResponse,
        )
        assert res_upd.status_code == 200

    def test_update_user_info_with_empty_header(self, app, register_auth_info):
        """
        1. Update user info with empty header
        2. Check that status code is 401
        """
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=None,
            type_response=AuthorizationRequiredResponse,
        )
        assert res_upd.status_code == 401
