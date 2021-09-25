import attr


@attr.s
class RegisterAuthResponse:
    access_token: str = attr.ib()


@attr.s
class AuthUser:
    header: dict = attr.ib()
    uuid: int = attr.ib()
