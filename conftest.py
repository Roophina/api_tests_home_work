import logging

import pytest

from fixtures.app import StoreApp
from fixtures.auth.model import RegisterAuthResponse, AuthUser
from fixtures.register.model import RegisterUser, RegisterUserResponse

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    # Todo: Add logger
    return StoreApp(url)


@pytest.fixture()
def register_auth(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_auth = app.auth.auth(data=data, type_response=RegisterAuthResponse)
    token = res_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    uuid = res_register.data.uuid
    return AuthUser(header=header, uuid=uuid)



def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),
