import attr


@attr.s
class RegisterAuthResponse:
    access_token: str = attr.ib()
