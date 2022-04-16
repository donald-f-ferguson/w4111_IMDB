import json
from DFF_Middleware.service_factory import ServiceFactory
from DFF_Middleware.context import Context


c_info = {
    "host": "localhost",
    "port": 3306,
    "user": "dbuser",
    "password": "dbuserdbuser",
    "db": "IMDBFixed"
}

s_factory = ServiceFactory()


def t2():

    Context._config_file = "../config.json"

    a_svc = s_factory.get_service("titles")
    res = a_svc.get_by_resource_id("/titles", "tt0109830", None)

    print("t2: Result = \n", json.dumps(res, indent=2, default=str))


def t3():

    """
    r_svc = UserDataService(c_info)
    res = r_svc.get_next_id()
    print("t3: Next ID = ", res)
    """
    pass


t2()
#t3()


