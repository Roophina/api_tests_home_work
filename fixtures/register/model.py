from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class RegisterUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return RegisterUser(username=fake.email(), password=fake.password())


@attr.s
class RegisterUserInt(BaseClass):
    username: int = attr.ib(default=None)
    password: int = attr.ib(default=None)

    @staticmethod
    def random():
        return RegisterUserInt(username=fake.pyint(), password=fake.pyint())


@attr.s
class RegisterUserResponse:
    message: str = attr.ib()
    uuid: int = attr.ib()


@attr.s
class RegisterUserResponseInvalid:
    message: str = attr.ib()
