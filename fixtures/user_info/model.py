from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Address:
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)


@attr.s
class AddUserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address() = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return AddUserInfo(
            phone=fake.phone_number(), email=fake.email(), address=address
        )


@attr.s
class AddUserResponse:
    message: str = attr.ib()


@attr.s
class UpdateUserResponse:
    message: str = attr.ib()


@attr.s
class Data:
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address() = attr.ib(default=None)


@attr.s
class IntBoolData:
    phone: bool = attr.ib(default=None)
    email: int = attr.ib(default=None)
    address: Address() = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return AddUserInfo(phone=fake.pybool(), email=fake.pyint, address=address)


@attr.s
class UserData:
    header: dict = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
    data_info: Data() = attr.ib(default=None)


@attr.s
class UpdateUserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address() = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return AddUserInfo(
            phone=fake.phone_number(), email=fake.email(), address=address
        )

    @staticmethod
    def empty():
        address = Address(city="", street="", home_number="")
        return AddUserInfo(phone="", email="", address=address)

    @staticmethod
    def big_random():
        address = Address(
            city=fake.city() * 100000,
            street=fake.street_name() * 100000,
            home_number=fake.building_number() * 100000,
        )
        return AddUserInfo(
            phone=fake.phone_number() * 100000,
            email=fake.email() * 100000,
            address=address,
        )


@attr.s
class InvalidToken:
    token: int = attr.ib(default=None)

    @staticmethod
    def random():
        return InvalidToken(token=fake.pyint())


@attr.s
class NotFoundResponse:
    pass


@attr.s
class UuidInvalidStr:
    uuid: int = attr.ib(default=None)

    @staticmethod
    def random():
        return UuidInvalidStr(uuid=fake.pystr())


@attr.s
class UuidInvalidBool:
    uuid: int = attr.ib(default=None)

    @staticmethod
    def random():
        return UuidInvalidBool(uuid=fake.pybool())


@attr.s
class UpdateInvalidDataResponse:
    pass
