from distutils import sysconfig
from distutils.extension import Extension
from distutils.core import setup
import platform
import os
import test1Cython
modules = []
build_dir = r"C:\Users\novasrodrigo\Desktop\qside\build_dir"
src_dir = os.path.abspath(os.path.join(build_dir, 'src'))
def create_file(c_files):
    setup(
        name="bii",
        version="1.1",
        script_name='setup.py',
        script_args=['build_ext'],
        packages=['biicode'],
        ext_modules=modules,
        )
    abs_path_c_files = [os.path.join(src_dir, c) for c in c_files]
    for c_file in abs_path_c_files:
        relfile = os.path.relpath(c_file, src_dir)
        filename = os.path.splitext(relfile)[0]
        extName = filename.replace(os.path.sep, ".")
        extension = Extension(extName,
                                sources=[c_file],
                                define_macros=[('PYREX_WITHOUT_ASSERTIONS',
                                                None)]  # ignore asserts in code
                                )
        modules.append(extension)

    if platform.system() != 'Windows':
        cflags = sysconfig.get_config_var('CFLAGS')
        opt = sysconfig.get_config_var('OPT')
        sysconfig._config_vars['CFLAGS'] = cflags.replace(' -g ', ' ')
        sysconfig._config_vars['OPT'] = opt.replace(' -g ', ' ')

    if platform.system() == 'Linux':
        ldshared = sysconfig.get_config_var('LDSHARED')
        sysconfig._config_vars['LDSHARED'] = ldshared.replace(' -g ', ' ')

if __name__ == "__main__":
    cfiles = test1Cython.bii_cythonize(True)
    create_file(cfiles)
