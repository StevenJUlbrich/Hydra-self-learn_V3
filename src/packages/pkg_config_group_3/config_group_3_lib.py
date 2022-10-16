from dataclasses import dataclass

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING


@dataclass
class ConfigGroup3:
    server: str = MISSING
    port: int = MISSING


@dataclass
class ConfigGroupFile5(ConfigGroup3):
    server: str = MISSING
    port: int = MISSING


@dataclass
class ConfigGroupFile6(ConfigGroup3):
    server: str = MISSING
    port: int = MISSING


def register_configs():
    configstore = ConfigStore.instance()
    configstore.store(
        group="config_group_3_lib/config_group_3", name="file_5", node=ConfigGroupFile5
    )
    configstore.store(
        group="config_group_3_lib/config_group_3", name="file_6", node=ConfigGroupFile6
    )
