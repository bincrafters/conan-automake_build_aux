from conans import ConanFile, tools
import os


class AutoMakeBuildAuxConan(ConanFile):
    name = "automake_build_aux"
    version = "1.16.1"
    license = "GPL-3.0-only"
    url = "https://github.com/bincrafters/conan-automake_build_aux"
    homepage = "https://www.gnu.org/software/automake/"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "auxiliary build files from automake distribution: compiler and ar-lib"
    no_copy_source = True
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "http://ftp.gnu.org/gnu/automake/automake-%s.tar.gz" % self.version
        tools.get(source_url, sha256="608a97523f97db32f1f5d5615c98ca69326ced2054c9f82e65bade7fc4c9dea8")
        os.rename("automake-" + self.version, self._source_subfolder)

    def package(self):
        self.copy(pattern="COPYING", dst="license", src=self._source_subfolder)
        self.copy(pattern="compile", src=os.path.join(self._source_subfolder, "lib"))
        self.copy(pattern="ar-lib", src=os.path.join(self._source_subfolder, "lib"))

    def package_id(self):
        self.info.header_only()
