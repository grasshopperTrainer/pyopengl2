#version 450 core

layout (location = 0) in vec4 vtx;
layout (location = 2) in vec4 fill_clr;
//layout (location = 2) in vec4 edge_clr;

uniform mat4 MM = mat4(1.0);
uniform mat4 VM = mat4(1.0);
uniform mat4 PM = mat4(1.0);

out vec4 fClrFill;

void main() {
    fClrFill = fill_clr;
    gl_Position = PM*VM*MM*vtx;
}
