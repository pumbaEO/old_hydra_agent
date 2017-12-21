from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = 'etc/hydra_agent.yml'

    def __call__(self, *args, **kwargs):
        with open(self.path) as f:
            return load(f, Loader=Loader)
