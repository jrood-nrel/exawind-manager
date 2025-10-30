# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumexpr(PythonPackage):
    """Fast numerical expression evaluator for NumPy"""

    homepage = "https://github.com/pydata/numexpr"
    url = "https://github.com/pydata/numexpr/archive/v2.7.0.tar.gz"

    license("MIT", checked_by="lgarrison")

    version("2.14.1", sha256="7cb4c2d5d686f366e1121c287f48c3964ae3ec2ecc559d64a12bb315beebbf9a")
    version("2.13.1", sha256="11ed30449f53647d02ae18fef8521ddcf28dc914650bd9289eecb6c687200b78")
    version("2.13.0", sha256="5d195fc922db64a171347795b4404c11cc0f3cd9088ac182539874c2c1e8dace")
    version("2.12.1", sha256="27e2143fdd80900838704b6e3d58fb98fb26a39982a82311870106f48e5e1628")
    version("2.12.0", sha256="f9be674524372576a26c3342ebe822b9fa9cb9b8b8344cebd6052aba1e81995c")
    version("2.11.0", sha256="5756eeb1c53bbbcbce2f343065ae6a128a947356621c6db6e57fb552790590ca")
    version("2.10.2", sha256="7e61a8aa4dacb15787b31c31bd7edf90c026d5e6dbe727844c238726e8464592")
    version("2.9.0", sha256="4df4163fcab20030137e8f2aa23e88e1e42e6fe702387cfd95d7675e1d84645e")
    version("2.8.8", sha256="10b377c6ec6d9c01349d00e16dd82e6a6f4439c8c2b1945e490df1436c1825f5")
    version("2.8.4", sha256="0e21addd25db5f62d60d97e4380339d9c1fb2de72c88b070c279776ee6455d10")
    version("2.8.3", sha256="389ceefca74eff30ec3fd03fc4c3b7ab3df8f22d1f235117a392ce702ed208c0")
    version("2.7.3", sha256="00d6b1518605afe0ed10417e0ff07123e5d531c02496c6eed7dd4b9923238e1e")
    version("2.7.2", sha256="7d1b3790103221feda07f4a93a4fa5c6654f46865197a677ca6f27eb5cb4e5ef")
    version("2.7.0", sha256="1923f038b90cc69635871968ed742be7775c879451c612f173c2547c823c9561")
    version("2.6.9", sha256="d57267bbdf10906f5ed7841b3484bec4af0494102b50e89ba316924cc7a7fd46")
    version("2.6.5", sha256="fe78a78e002806e87e012b6105f3b3d52d47fc7a72bafb56341fcec7ce02cfd7")
    version("2.6.1", sha256="e92c83d066fa8da63864d69b5f218287cc31437ae844db77390f2183123aab22")
    version("2.5", sha256="4ca111a9a27c9513c2e2f5b70c0a84ea69081d7d8e4512d4c3f26a485292de0d")
    version("2.4.6", sha256="2681faf55a3f19ba4424cc3d6f0a10610ebd49f029f8453f0ba64dd5c0fe4e0f")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.7:", when="@2.8.3:", type=("build", "run"))
    depends_on("python@3.9:", when="@2.8.7:", type=("build", "run"))
    depends_on("python@3.10:", when="@2.11.0:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@2:", when="@2.10.2:", type="build")
    depends_on("py-numpy@1.23:", when="@2.10.2:", type="run")
    depends_on("py-numpy@1.13.3:1.25", type=("build", "run"), when="@2.8.3:2.9")
    # https://github.com/pydata/numexpr/issues/397
    depends_on("py-numpy@1.7:1.22", type=("build", "run"), when="@:2.7")
    # https://github.com/pydata/numexpr/pull/478
    depends_on("py-numpy@:1", when="@:2.9", type=("build", "run"))

    # Historical dependencies
    depends_on("py-packaging", type=("build", "run"), when="@2.8.3")
