from distutils.ccompiler import new_compiler
import setuptools #agregarla SIEMPRE aunque no se use
if __name__ == '__main__':
    compiler = new_compiler()
    compiler.compile([r'C:\Users\novasrodrigo\Desktop\qside\Metodo casting cython\main.c'],)
    compiler.link_executable(['main.o'], 'main', r"C:\Users\novasrodrigo\Desktop\qside\build_dir")