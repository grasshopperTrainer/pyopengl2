from doodler import *
from mkernel import Model, Tgl
from wkernel import Window


class MyWindow(Window):
    def __init__(self):
        super().__init__(500, 500, 'my window 1', monitor=None, shared=None)
        self.framerate = 60
        # enable camera move
        o = 100
        self.devices.cameras[0].tripod.lookat((o, o, o), (0, 0, 0), (0, 0, 1))
        self.devices.cameras.attach_fps_dolly(0)

        # create model
        self.model = Model()
        # create triangles
        e = 50
        t0 = Tgl([0, 0, 0], [e, 0, 0], [0, e, 0])
        t1 = Tgl([0, 0, 0], [0, e, 0], [0, 0, e])
        t2 = Tgl([0, 0, 0], [e, 0, 0], [0, 0, e])
        # set fill color
        i, a = 1, 1
        t0.clr_fill = i, 0, 0, a
        t1.clr_fill = 0, i, 0, a
        t2.clr_fill = 0, 0, i, a
        # set edge color
        for t in (t0, t1, t2):
            t.edge_clr = 1, 1, 1, 1
            t.edge_thk = 5
        # build model
        # self.model.append_shape(t0)
        # self.model.append_shape(t1)
        # self.model.append_shape(t2)

    def draw(self, frame_count=None):
        with self.devices.panes[0] as p:
            with self.devices.cameras[0] as c:
                p.clear(.5, .5, .5, 1)
                # e = 100
                self.model.test_render()
                # self.model.intersect(c.frusrum_ray(*v.local_cursor()))

MyWindow().run_all(1)
