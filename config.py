TEMPLATE_DIR = "/etc/consul-template/templates"
TEMPLATE_FILE = "nginx_split_upstream.j2"
OUTPUT_DIR = "/usr/local/openresty/nginx/conf/conf.d/wan/"
OPENRESTY_RELOAD_CMD = "openresty -s reload"

# CONSUL_HOST = "127.0.0.1"
# CONSUL_PORT = 8500
CONSUL_HOST = "10.10.10.135"
CONSUL_PORT = 8500


SERVICE_NAMES = [
    "diplo-service",
    "gary-service",
    "dave-service",
    "gmoney-service",
    "gmoney-service",
    "illia-service",
    "lex-service",
]

NODES = [
    (
        "diplo",
        [
            "diplo.us.gaianet.network",
            "0x4d21cedb900232b22801e0632b5b2a646d732a2e.us.gaianet.network",
        ],
    ),
    (
        "illia",
        [
            "muadao.gaianet.network",
            "illia-bot.gaianet.network",
        ],
    ),
    (
        "gary",
        [
            "0xe95310de2ad8f09f7b31699c7445f3787aa4b7d0.us.gaianet.network",
            "0x19a8e4a397cab67b97e7b537255ad903a8a9d277.us.gaianet.network",
        ],
    ),
    (
        "lex",
        [
            "0x02c8413587a23dc6807a04558f4231c7d482a812.gaianet.network",
        ],
    ),
    (
        "dave",
        [
            "0x62b4800e0849a8b448f90a9341c26709018b6489.us.gaianet.network",
        ],
    ),
    (
        "gmoney",
        [
            "0xc21fb69eb908b3fd74f0ad84111146197ab3e3c2.us.gaianet.network",
            "0xdcd781b14684e98a29a2ad851c2b71d999fa4008.us.gaianet.network",
        ],
    ),
]
