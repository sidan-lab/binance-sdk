from binance.lib.utils import check_required_parameter, check_required_parameters


def balance(self, **kwargs):
    """ """

    url_path = "/fapi/v3/balance"
    payload = {**kwargs}
    return self.sign_request("GET", url_path, payload)
