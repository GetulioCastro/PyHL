# PyHL
A Python Home Library Manager


## How to contribute to the project

1. Clone the repository to your machine. `git clone git@github.com:Riverfount/PyHL.git`
1. For the second step we need to have Poetry installed. If you don't have
the Poetry installed: `pip install poetry`
1. Access the directory of the project and install by Poetry `poetry install`
1. Export Django Settings envvar: `export DJANGO_SETTINGS_MODULE=djhl.settings`
1. Copy contrib/settings_example.yaml to root of project and change its name to settings.py, and change `{user}` to
your user on the system: `cp contrib/settings_example.yaml settings.yaml`
1. Create a .secrets.toml file with the Django Secret Key. Below we have a sample of this file.
1. Test your installation: `python mange.py runserver`

#### .secrets.toml file example
```toml
[default]
SECRET_KEY = "t_21su#f56q3u15je6dsi5!jhxhz6#l*cbgr7%efk^$$@e)%zl"
```
