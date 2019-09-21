import os
from wsgiref.simple_server import make_server as make_wsgi_server
import configparser
from ankisyncd import settings
from ankisyncd.sync_app import SyncApp


class SyncAppController:
    sync_server_app_class = SyncApp

    def __init__(self):
        self.config = None
        self.server = None

    @staticmethod
    def get_config_from_os_env():
        conf = {}
        key_in_os_envs_for_anki = [os_env for os_env in os.environ if os_env.startswith('ANKISYNCD_')]
        for key in key_in_os_envs_for_anki:
            conf_key = key[10:].lower()
            conf[conf_key] = os.getenv(key)
        return conf

    @staticmethod
    def get_config_from_files():
        parser = configparser.ConfigParser()
        parser.read(settings.config_path)
        conf = parser['sync_app']
        return conf

    def make_server(self):
        self.server = make_wsgi_server(
            host=self.config['host'],
            port=int(self.config['port']),
            app=self.sync_server_app_class(self.config)
        )

    def load_config(self):
        self.config = {}
        self.config.update(self.get_config_from_files())
        self.config.update(self.get_config_from_os_env())

    def run_server(self):
        self.server.serve_forever()


if __name__ == "__main__":
    controller = SyncAppController()
    controller.load_config()
    controller.make_server()
    controller.run_server()
