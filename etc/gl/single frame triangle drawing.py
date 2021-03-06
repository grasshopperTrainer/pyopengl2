from UVT import Window
import UVT.pipeline as comp
import glfw
import numpy as np

window1 = Window.new_window(200,200, 'f', monitor=None, shared=None)

with window1 as w:
    vertex = [[-1, -1, 0], [1, -1, 0], [0, 1, 0], [1,1,0]]
    va = comp.ConSingleNamedData('coord', vertex, 'f')
    vbo = comp.ConVertexBuffer(w)
    vao = comp.ConVertexArray(w)
    #
    buffer_pusher = comp.PushBufferData(w)
    enabler = comp.EnableVertexAttribute(w)

    buffer_pusher.in1_data = va.out0_ndata
    buffer_pusher.in0_bffr = vbo.out0_vrtx_bffr
    enabler.in0_vrtx_arry = vao.vrtx_arry
    enabler.vrtx_attr = va.out0_ndata
    #
    joiner = comp.JoinVrtxArryVrtxBffr(w)
    joiner.in0_vrtx_arry = vao.vrtx_arry
    joiner.out0_vrtx_bffr = vbo.out0_vrtx_bffr

    tri_drawer = comp.RenderArray(w, joiner.vrtx_arry_out, comp.Bound(1, 4))

    # tri_drawer.vrtx_arry = joiner.vrtx_arry_out

    print(tri_drawer.render_attempt)

Window.run_all(1)