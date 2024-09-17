import uuid

from consul import Check, Consul


def register_service(name, host):
    consul = Consul(
        host="10.10.10.135", port=8500
    )  # 根据实际情况修改 Consul 的地址和端口

    service_name = f"{name}-service"
    service_id = f"{name}-service-{uuid.uuid4()}"
    service_address = f"{host}"
    service_port = 443

    # 定义健康检查
    check = Check.http(
        "https://{0}/echo".format(service_address),
        interval="10s",
        timeout="1s",
    )

    # 注册服务
    consul.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=service_address,
        port=service_port,
        check=check,
    )

    print(f"服务 {service_name} 已注册")


# 注销服务
def deregister_service(service_id):
    consul = Consul(
        host="10.10.10.135", port=8500
    )  # 根据实际情况修改 Consul 的地址和端口
    consul.agent.service.deregister(service_id)


# 根据服务名 注销所有
def deregister_all_services(name):
    consul = Consul(host="10.10.10.135", port=8500)
    services = consul.agent.services()
    for service_id, service in services.items():
        if service["Service"] == f"{name}-service":
            consul.agent.service.deregister(service_id)
            print(f"服务 {name} 已注销")


def add_services(name, hosts):
    for host in hosts:
        register_service(name, host)


if __name__ == "__main__":
    # https://www.notion.so/mellow-trader-6de/KOL-with-3D-avatar-c32c47a78cd34e82bef2a76336414ca5?pvs=4
    add_services(
        "diplo",
        [
            "diplo.us.gaianet.network",
            "0x4d21cedb900232b22801e0632b5b2a646d732a2e.us.gaianet.network",
        ],
    )

    add_services(
        "illia",
        [
            "muadao.gaianet.network",
            "illia-bot.gaianet.network",
        ],
    )

    add_services(
        "gary",
        [
            "0xe95310de2ad8f09f7b31699c7445f3787aa4b7d0.us.gaianet.network",
            "0x19a8e4a397cab67b97e7b537255ad903a8a9d277.us.gaianet.network",
        ],
    )

    add_services(
        "lex",
        [
            "0x02c8413587a23dc6807a04558f4231c7d482a812.gaianet.network",
        ],
    )

    add_services(
        "dave",
        [
            "0x62b4800e0849a8b448f90a9341c26709018b6489.us.gaianet.network",
        ],
    )

    add_services(
        "gmoney",
        [
            "0xc21fb69eb908b3fd74f0ad84111146197ab3e3c2.us.gaianet.network",
            "0xdcd781b14684e98a29a2ad851c2b71d999fa4008.us.gaianet.network",
        ],
    )

    # for name in ["diplo", "illia", "gary", "lex", "dave", "gmoney"]:
    #     deregister_all_services("diplo")
