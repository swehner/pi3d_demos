#include std_head_fs.inc

varying vec2 texcoordout;
varying float dist;

void main(void) {
#include std_main_uv.inc
  vec4 mat = vec4(unib[1], 1.0); // ------ basic colour from material vector
  texc[0]=mat[0];
  texc[1]=mat[1];
  texc[2]=mat[2];

  gl_FragColor = (1.0 - ffact) * texc + ffact * vec4(unif[4], unif[5][1]); // ------ combine using factors
  gl_FragColor.a *= unif[5][2];
}

