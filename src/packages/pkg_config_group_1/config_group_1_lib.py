from dataclasses import dataclass
from omegaconf import MISSING
from hydra.core.config_store import ConfigStore


@dataclass
class ConfigGroup1:
    site: str = MISSING
    port: int = MISSING


@dataclass
class ConfigGroupFile1(ConfigGroup1):
    site: str = MISSING
    port: int = MISSING


@dataclass
class ConfigGroupFile2(ConfigGroup1):
    site: str = MISSING
    port: int = MISSING


def register_configs():
    cs = ConfigStore.instance()
    cs.store(
        group="config_group_1_lib/config_group_1", name="file_1", node=ConfigGroupFile1
    )
    cs.store(
        group="config_group_1_lib/config_group_1", name="file_2", node=ConfigGroupFile2
    )
