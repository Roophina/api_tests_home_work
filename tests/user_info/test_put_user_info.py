import pytest

from fixtures.auth.model import NotAuthorizationResponse
from fixtures.user_info.model import (
    UpdateUserInfo,
    UpdateUserResponse,
    InvalidToken,
    NotFoundResponse,
    UuidInvalidStr,
    UuidInvalidBool,
    IntBoolData,
    UpdateInvalidDataResponse,
)


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
            type_response=NotAuthorizationResponse,
        )
        assert res_upd.status_code == 401

    def test_update_user_info_with_invalid_token(self, app, register_auth_info):
        """
        1. Update user info with invalid header
        2. Check that status code is 401
        """
        data = UpdateUserInfo.random()
        token = InvalidToken.random()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header={"Authorization": f"JWT {token}"},
            type_response=NotAuthorizationResponse,
        )
        assert res_upd.status_code == 401

    @pytest.mark.xfail(reason="Ожидается json в теле ответа, а приходит html")
    def test_update_user_info_with_empty_uuid(self, app, register_auth_info):
        """
        1. Update user info with empty uuid
        2. Check that status code is 404
        """
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(
            uuid=None,
            data=data,
            header=register_auth_info.header,
            type_response=NotFoundResponse,
        )
        assert res_upd.status_code == 404

    @pytest.mark.xfail(reason="Ожидается json в теле ответа, а приходит html")
    @pytest.mark.parametrize(
        "uuid_invalid", [UuidInvalidStr.random(), UuidInvalidBool.random()]
    )
    def test_update_user_info_with_invalid_uuid(
        self, app, register_auth_info, uuid_invalid
    ):
        """
        1. Update user info with invalid uuid
        2. Check that status code is 404
        """
        data = UpdateUserInfo.random()
        res_upd = app.user_info.update_user_info(
            uuid=uuid_invalid,
            data=data,
            header=register_auth_info.header,
            type_response=NotFoundResponse,
        )
        assert res_upd.status_code == 404

    def test_update_user_info_with_empty_data(self, app, register_auth_info):
        """
        1. Update user info with empty data
        2. Check that status code is 200
        """
        data = UpdateUserInfo.empty()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=register_auth_info.header,
            type_response=UpdateUserResponse,
        )
        assert res_upd.status_code == 200

    @pytest.mark.xfail(reason="Ожидается код ответа 422, а приходит 200")
    def test_update_user_info_with_invalid_data(self, app, register_auth_info):
        """
        1. Update user info with invalid data
        2. Check that status code is 422
        """
        data = IntBoolData.random()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=register_auth_info.header,
            type_response=UpdateInvalidDataResponse,
        )
        assert res_upd.status_code == 422

    @pytest.mark.xfail(reason="Ожидается код ответа 422, а приходит 200")
    def test_update_info_with_big_data(self, app, register_auth_info):
        """
        1. Update user info with big data
        2. Check that status code is 422
        """
        data = UpdateUserInfo.big_random()
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=register_auth_info.header,
            type_response=UpdateInvalidDataResponse,
        )
        assert res_upd.status_code == 422

    def test_update_info_unchanged_data(self, app, register_auth_info):
        """
        1. Update user info with unchanged data
        2. Check that status code is 200
        """
        data = register_auth_info.data_info
        res_upd = app.user_info.update_user_info(
            uuid=register_auth_info.uuid,
            data=data,
            header=register_auth_info.header,
            type_response=UpdateUserResponse,
        )
        assert res_upd.status_code == 200
