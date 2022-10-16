from dataclasses import dataclass

import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, OmegaConf

import packages.pkg_config_group_1.config_group_1_lib as config_group_1_lib
import packages.pkg_config_group_2.config_group_2_lib as config_group_2_lib
import packages.pkg_config_group_3.config_group_3_lib as config_group_3_lib


@dataclass
class Config:
    config_group_1: config_group_1_lib.ConfigGroup1 = MISSING
    config_group_2: config_group_2_lib.ConfigGroup2 = MISSING
    config_group_3: config_group_3_lib.ConfigGroup3 = MISSING
    debug: bool = False


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)

config_group_1_lib.register_configs()
config_group_2_lib.register_configs()
config_group_3_lib.register_configs()


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(cfg["config_group_1"]["site"])  # type: ignore
    print(cfg.config_group_1.site)
    print(cfg.config_group_2.username)
    print(cfg.config_group_3.server)


if __name__ == "__main__":
    main()
