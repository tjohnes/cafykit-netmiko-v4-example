import logging

import pytest
from netmiko import ConnectHandler
from netmiko.exceptions import ConfigInvalidException

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def r1():
    return ConnectHandler(
        device_type="cisco_xr",
        host="localhost",
        port=57011,
        username="user",
        password="pass",
        session_log="netmiko.log",
    )


def test_disabled_config(r1):
    for _ in range(100):
        with pytest.raises(ConfigInvalidException):
            r1.send_config_set("zzz", error_pattern="Invalid input")
        r1.exit_config_mode()
