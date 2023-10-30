from rest_framework.exceptions import APIException


class NoActiveAccountsError(APIException):
    status_code = 400
    default_detail = "Bad Request"
