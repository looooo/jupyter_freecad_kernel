import sys
from ipykernel.ipkernel import IPythonKernel as Kernel


class FreeCADKernel(Kernel):
    implementation = 'FreeCAD'
    implementation_version = '0.1'
    banner = "notebook conection to freecad"

    def start(self):
        Kernel.start(self)
        self.do_execute("%gui qt", False)
        sys.path.append("/usr/lib/freecad/lib/")
        import FreeCADGui
        self.win = FreeCADGui.showMainWindow()


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=FreeCADKernel)
