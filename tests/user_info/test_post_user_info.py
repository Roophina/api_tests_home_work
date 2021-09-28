from fixtures.user_info.model import AddUserInfo, AddUserResponse


class TestPostUserInfo:
    def test_add_user_info(self, app, register_auth):
        """
        1. Add user info with valid data
        2.Check that status code is 200
        """
        data = AddUserInfo.random()
        res_add = app.user_info.add_user_info(
            uuid=register_auth.uuid,
            data=data,
            header=register_auth.header,
            type_response=AddUserResponse,
        )
        assert res_add.status_code == 200
