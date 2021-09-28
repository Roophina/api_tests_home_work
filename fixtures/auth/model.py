import attr


@attr.s
class RegisterAuthResponse:
    access_token: str = attr.ib()


@attr.s
class AuthUser:
    header: dict = attr.ib()
    uuid: int = attr.ib()


@attr.s
class NotAuthorizationResponse:
    description: str = attr.ib()
    error: str = attr.ib()
    status_code: int = attr.ib()
