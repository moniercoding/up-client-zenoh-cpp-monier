from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get, replace_in_file, rm, rmdir
import os

class UpClientZenoh(ConanFile):
    name = "up-client-zenoh-cpp"
    package_type = "library"
    license = "Apache-2.0 license"
    homepage = "https://github.com/eclipse-uprotocol"
    url = "https://github.com/conan-io/conan-center-index"
    description = "C++ uLink Library for zenoh transport"
    topics = ("ulink client", "transport")
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    conan_version = None
    generators = "CMakeDeps"
    version = "0.1"
    exports_sources = "CMakeLists.txt", "lib/*"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": False,
    }

    def requirements(self):
        self.requires("up-cpp/0.1")
        self.requires("spdlog/1.13.0")
        self.requires("fmt/10.2.1")
        self.requires("protobuf/3.21.12")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["up-client-zenoh-cpp"]
