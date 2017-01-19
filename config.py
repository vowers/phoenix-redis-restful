class Config(object):
    phoenix_server_url = "http://10.10.10.168:8765"
    redis_client_url = [
        "http://127.0.0.1:8000/api/getredis/",
        "http://127.0.0.1:8000/api/getredis/",
        "http://127.0.0.1:8000/api/getredis/"
    ]
    redis_nodes = [
        {
            'host': '',
            'port': 
        },
        {
            'host': '',
            'port': 
        },
        {
            'host': '',
            'port': 
        },
        {
            'host': '',
            'port': 
        },
        {
            'host': '',
            'port': 
        },
        {
            'host': '',
            'port': 
        },
    ]
    mysql_ip = ""
    mysql_username = ""
    mysql_password = ""
    mysql_dbname = ""

    def setting(self):
        pass