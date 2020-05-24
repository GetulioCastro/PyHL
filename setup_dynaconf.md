# Steps to set up Dynaconf on Django Project

## Below we have a step by step to set up Dynaconf on Django Project

1. `export DJANGO_SETTINGS_MODULE=djhl.settings`
1. `dynaconf init --django=djhl/settings.py`
1. `poetry add PyYaml`
1. `dynaconf list -o settings.yaml`
1. removemos a SECRET_KEY do settings.yaml  
1. colocamos a SECRET_KEY no arquivo .secrets.toml

