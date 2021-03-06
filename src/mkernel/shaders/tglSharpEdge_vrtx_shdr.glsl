#version 450 core

layout (location = 0) in vec4 vtx;
layout (location = 1) in float edge_thk;
layout (location = 2) in vec4 edge_clr;

layout (location = 0) uniform mat4 MM = mat4(1.0);
layout (location = 1) uniform mat4 VM = mat4(1.0);
layout (location = 2) uniform mat4 PM = mat4(1.0);

out vsOut {
    float edgeThk;
    vec4 edgeClr;
} vs_out;

void main() {
    // for geometry shader
    vs_out.edgeThk = edge_thk;
    vs_out.edgeClr = edge_clr;
    gl_Position = vtx;
}
