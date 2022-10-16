from dataclasses import dataclass

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING


@dataclass
class ConfigGroup2:
    username: str = MISSING
    password: str = MISSING
    level: int = MISSING


@dataclass
class ConfigGroupFile3(ConfigGroup2):
    username: str = MISSING
    password: str = MISSING
    level: int = MISSING


@dataclass
class ConfigGroupFile4(ConfigGroup2):
    username: str = MISSING
    password: str = MISSING


def register_configs():
    configstore = ConfigStore.instance()
    configstore.store(
        group="config_group_2_lib/config_group_2", name="file_3", node=ConfigGroupFile3
    )
    configstore.store(
        group="config_group_2_lib/config_group_2", name="file_4", node=ConfigGroupFile4
    )
