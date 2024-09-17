import uuid

from consul import Check, Consul

from config import CONSUL_HOST, CONSUL_PORT, NODES, SERVICE_NAMES


def register_service(name, host):
    consul = Consul(
        host=CONSUL_HOST, port=CONSUL_PORT
    )  # 根据实际情况修改 Consul 的地址和端口

    service_name = f"{name}-service"
    service_id = f"{name}-service-{uuid.uuid4()}"
    service_address = f"{host}"
    service_port = 443

    # 定义健康检查
    check = Check.http(
        "https://{0}/echo".format(service_address),
        interval="10s",
        timeout="3s",
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
        host=CONSUL_HOST, port=CONSUL_PORT
    )  # 根据实际情况修改 Consul 的地址和端口
    consul.agent.service.deregister(service_id)


# 根据服务名 注销所有
def deregister_all_services(service_names):
    consul = Consul(host=CONSUL_HOST, port=CONSUL_PORT)
    services = consul.agent.services()
    for service_id, service in services.items():
        if service["Service"] in service_names:
            consul.agent.service.deregister(service_id)
            server_name = service["Service"]
            print(f"服务 {server_name} 已注销")


def add_services(name, hosts):
    for host in hosts:
        register_service(name, host)


if __name__ == "__main__":
    # https://www.notion.so/mellow-trader-6de/KOL-with-3D-avatar-c32c47a78cd34e82bef2a76336414ca5?pvs=4

    deregister_all_services(SERVICE_NAMES)

    for node in NODES:
        add_services(node[0], node[1])
