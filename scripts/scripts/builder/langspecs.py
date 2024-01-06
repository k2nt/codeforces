from enum import Enum
from dataclasses import dataclass


class CppVersion(Enum):
    """Accepted CPP versions."""
    CPP11 = 'c++11'
    CPP14 = 'c++14'
    CPP17 = 'c++17'
    CPP20 = 'c++20'


@dataclass(init=False, frozen=True)
class CppLangSpecs:
    """CPP language specifications."""
    accepted_versions = CppVersion
    obj_build_path: str = 'cpp/obj'
    exec_build_path: str = 'cpp'
    