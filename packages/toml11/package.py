from spack import *


class Toml11(CMakePackage):
    """toml11 is a C++11 (or later) header-only toml parser/encoder depending only on C++ standard library.
    Supported TOML standard: TOML v1.0.0-rc.2
    """

    homepage = "https://github.com/ToruNiina/toml11"
    url      = "https://github.com/ToruNiina/toml11/archive/v3.6.0.tar.gz"
    git      = "https://github.com/ToruNiina/toml11.git"

    # notify when the package is updated.
    maintainers = ['alephpiece']

    version('3.6.0', sha256='39e8d651db346ae8c7e3b39d6338a37232b9af3bba36ade45b241bf105c2226c')
    version('3.5.0', sha256='fc613874c6e80dc740134a7353cf23c7f834b59cd601af84ab535ee16a53b1c3')
    version('3.4.0', sha256='bc6d733efd9216af8c119d8ac64a805578c79cc82b813e4d1d880ca128bd154d')
    version('3.3.1', sha256='0c1b29e1a2873a1b1f6d0865a2966a2d3fd9155aeccb6139cd5af22f70b0b08f')
    version('3.3.0', sha256='b29995475922fae3095445219d36733ef18976abdc85685d0804ee3ea04f09c0')
    version('3.2.1', sha256='370f17409cfcbf3f629728ed7ec2e1573544058615fb5d066f4f7c14693143a9')
    version('3.2.0', sha256='3d54cac38ea24477190e0535377e824bf06562970ef4d35b59aa9729437e1019')
    version('3.1.0', sha256='3a118f32e5343998f37be9807c72fd11c3168fe12a5b1abfdc0f1e60de6380a4')
