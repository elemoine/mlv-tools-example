import os
import pathlib

import yaml

if "PIPELINE_CLIENT" not in os.environ:
    raise Exception('Env var "PIPELINE_CLIENT" is not defined')

client = os.environ["PIPELINE_CLIENT"]

client_dir = pathlib.Path("..", "..", client)
client_conf_dir = client_dir / "conf"
client_conf_file = client_conf_dir / "docstring_conf.yml"

with open(str(client_conf_file)) as f:
    conf = yaml.safe_load(f)

for k, v in conf.items():
    conf[k] = str(client_dir / v)
