from .._opengl import *


class ConDataComponent(OpenglNode):
    """
    Parent for data nodes using numpy array
    """
    val_out = Output(None)

    def __init__(self, data):
        if isinstance(data, (tuple, list)):
            self.val_out = FloatVector(np.array(data, dtype=self._dtype))
        elif isinstance(data, np.array):
            self.val_out = FloatVector(data)
        else:
            raise NotImplementedError

    @property
    def is_renderable(self):
        return False


class ConFloatVector(ConDataComponent):
    _dtype = 'f'


class ConUnsignedIntVector(ConDataComponent):
    _dtype = 'uint'


class Window(OpenglNode):
    window = Output(None)

    def __init__(self, w):
        self.window = w


class Listener(NodeBody):
    in0_listento = Input(has_siblings=True)
    out0_listened = Output(has_siblings=True)

    def calculate(self, listentos):
        return listentos