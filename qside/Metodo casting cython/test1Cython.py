from Cython.Build import cythonize
import os

biicode_pkg_path = r"C:\Users\novasrodrigo\Desktop\qside\biicode_pkg_path"
biicode_python_path = os.path.dirname(biicode_pkg_path)
build_dir = r"C:\Users\novasrodrigo\Desktop\qside\build_dir"
src_dir = os.path.abspath(os.path.join(build_dir, 'src'))
if not os.path.exists(src_dir):
   os.makedirs(src_dir)
ignored_files = ['__init__.py']
included_dirs = [os.path.join(biicode_pkg_path, dir_) for dir_ in ['client', 'common', "main"]]

def bii_cythonize(force_compile):
    '''
    Creates c files from your source python
    Params:
        force_compile: boolean, if true compiles regardeless 
                        of whether the file has changed or not
    Returns:
        list of c files relative to biicode_pkg_path
    '''

    c_files = []
    for dir_ in included_dirs:
        for dirname, dirnames, filenames in os.walk(dir_):
            if 'test' in dirnames:
                dirnames.remove('test')

            for filename in filenames:
                file_ = os.path.join(dirname, filename)
                stripped_name = os.path.relpath(file_, biicode_python_path)
                file_name, extension = os.path.splitext(stripped_name)

                if extension == '.py':
                    target_file = os.path.join(src_dir, file_name + '.c')
                    if filename not in ignored_files:
                        c_files.append(stripped_name.replace('.py', '.c'))
                        file_dir = os.path.dirname(target_file)
                        if not os.path.exists(file_dir):
                            os.makedirs(file_dir)

                        extension = cythonize(stripped_name,
                                                force=force_compile,
                                        build_dir=src_dir)

    return c_files


# c_files=bii_cythonize(force_compile=True)