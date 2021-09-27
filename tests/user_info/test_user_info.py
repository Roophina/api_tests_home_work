from fixtures.user_info.model import AddUserInfo, AddUserResponse, UpdateUserInfo, UpdateUserResponse


class TestUserInfo:
    def test_add_user_info(self, app, register_auth):
        """
                1.
                2.
                3.
                #"""
        data = AddUserInfo.random()
        res_add = app.user_info.add_user_info(uuid=register_auth.uuid, data=data, header=register_auth.header,
                                              type_response=AddUserResponse)
        assert res_add.status_code == 200

    def test_update_user_info(self, app, register_auth_info):
        """
                        1.
                        2.
                        3.
                        #"""
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(uuid=register_auth_info.uuid, data=data,
                                                 header=register_auth_info.header,
                                                 type_response=UpdateUserResponse)
        assert res_upd.status_code == 200

    def test_update_user_info_with_empty_header(self, app, register_auth_info):
        """
                        1.
                        2.
                        3.
                        #"""
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(uuid=register_auth_info.uuid, data=data,
                                                 header=None,
                                                 type_response=None)
        assert res_upd.status_code == 401
