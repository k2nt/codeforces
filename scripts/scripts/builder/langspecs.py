from enum import Enum
from dataclasses import dataclass


import scripts.common.filepath as fp


class CppVersion(Enum):
    """Accepted CPP versions."""
    CPP11 = 'c++11'
    CPP14 = 'c++14'
    CPP17 = 'c++17'
    CPP20 = 'c++20'


@dataclass(init=False, frozen=True)
class CppLangSpecs:
    """CPP language specifications."""
    accepted_versions = list(CppVersion)
    default_version = CppVersion.CPP17
    exec_build_path: str = fp.to_pwd_path('cpp/xc')
    