from requests import Response

from fixtures.user_info.model import AddUserInfo, UpdateUserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_ADD = "/user_info/{}"

    @log("Add info for user")
    def add_user_info(
        self, uuid: int, data: AddUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_ADD.format(uuid)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    PUT_UPDATE = "/user_info/{}"

    @log("Update user's info")
    def update_user_info(
        self, uuid: int, data: UpdateUserInfo, header=None, type_response=None
    ) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoUpdate
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_UPDATE.format(uuid)}",
            json=data.to_dict(),
            headers=header,
        )
        return self.structure(response, type_response=type_response)
