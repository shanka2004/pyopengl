'''OpenGL extension ARB.draw_elements_base_vertex

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/draw_elements_base_vertex.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_draw_elements_base_vertex'
_DEPRECATED = False

glDrawElementsBaseVertex = platform.createExtensionFunction( 
'glDrawElementsBaseVertex',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLenum,ctypes.c_void_p,constants.GLint,),
doc='glDrawElementsBaseVertex(GLenum(mode), GLsizei(count), GLenum(type), c_void_p(indices), GLint(basevertex)) -> None',
argNames=('mode','count','type','indices','basevertex',),
deprecated=_DEPRECATED,
)

glDrawRangeElementsBaseVertex = platform.createExtensionFunction( 
'glDrawRangeElementsBaseVertex',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,constants.GLsizei,constants.GLenum,ctypes.c_void_p,constants.GLint,),
doc='glDrawRangeElementsBaseVertex(GLenum(mode), GLuint(start), GLuint(end), GLsizei(count), GLenum(type), c_void_p(indices), GLint(basevertex)) -> None',
argNames=('mode','start','end','count','type','indices','basevertex',),
deprecated=_DEPRECATED,
)

glDrawElementsInstancedBaseVertex = platform.createExtensionFunction( 
'glDrawElementsInstancedBaseVertex',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLenum,ctypes.c_void_p,constants.GLsizei,constants.GLint,),
doc='glDrawElementsInstancedBaseVertex(GLenum(mode), GLsizei(count), GLenum(type), c_void_p(indices), GLsizei(primcount), GLint(basevertex)) -> None',
argNames=('mode','count','type','indices','primcount','basevertex',),
deprecated=_DEPRECATED,
)

glMultiDrawElementsBaseVertex = platform.createExtensionFunction( 
'glMultiDrawElementsBaseVertex',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLsizeiArray,constants.GLenum,ctypes.POINTER(ctypes.c_void_p),constants.GLsizei,arrays.GLintArray,),
doc='glMultiDrawElementsBaseVertex(GLenum(mode), GLsizeiArray(count), GLenum(type), POINTER(ctypes.c_void_p)(indices), GLsizei(primcount), GLintArray(basevertex)) -> None',
argNames=('mode','count','type','indices','primcount','basevertex',),
deprecated=_DEPRECATED,
)


def glInitDrawElementsBaseVertexARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )