class NoFreeVM(Exception):
    code = 500

    def __init__(self, msg):
        self.msg = msg


class VirtualMachineProblem(Exception):
    code = 500

    def __init__(self, msg):
        self.msg = msg


class VolumeImageProblem(Exception):
    code = 500

    def __init__(self, msg):
        self.msg = msg


class VMNotFound(Exception):
    code = 404

    def __init__(self, msg):
        self.msg = msg