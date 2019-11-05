from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):

    def test(self):
        assert os.path.isfile(os.path.join(self.deps_cpp_info["automake_build_aux"].rootpath, "compile"))
        assert os.path.isfile(os.path.join(self.deps_cpp_info["automake_build_aux"].rootpath, "ar-lib"))
