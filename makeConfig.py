#!/usr/bin/env python3
import os
import subprocess
import sys

import requests
from jinja2 import Environment, FileSystemLoader
from config import (
    CONSUL_HOST,
    CONSUL_PORT,
    SERVICE_NAMES,
    TEMPLATE_DIR,
    TEMPLATE_FILE,
    OUTPUT_DIR,
    OPENRESTY_RELOAD_CMD,
)
# 配置参数


def get_service_instances(service_name):
    url = f"http://{CONSUL_HOST}:{CONSUL_PORT}/v1/catalog/service/{service_name}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching service {service_name}: {e}", file=sys.stderr)
        return []


def fetch_services():
    services = []
    for service_name in SERVICE_NAMES:
        instances = get_service_instances(service_name)
        service_info = {"name": service_name, "instances": instances}
        services.append(service_info)
    return services


def render_template(services):
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template(TEMPLATE_FILE)
    return template.render(services=services)


def write_config(service_name, rendered_config):
    # 生成独立的配置文件名，例如 diplo.conf
    config_filename = (
        f"{service_name.replace('-service', '')}-all.us.gaianet.network.conf"
    )
    output_path = os.path.join(OUTPUT_DIR, config_filename)
    try:
        with open(output_path, "w") as f:
            f.write(rendered_config)
        os.chmod(output_path, 0o644)
        print(f"Configuration written to {output_path}")
    except IOError as e:
        print(f"Failed to write config file {output_path}: {e}", file=sys.stderr)


def reload_openresty():
    try:
        subprocess.run(OPENRESTY_RELOAD_CMD.split(), check=True)
        print("OpenResty reloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reload OpenResty: {e}", file=sys.stderr)


def main():
    services = fetch_services()

    for service in services:
        print(f"Rendering config for {service['name']}")
        rendered_config = render_template([service])
        write_config(service["name"], rendered_config)
    reload_openresty()


if __name__ == "__main__":
    main()
