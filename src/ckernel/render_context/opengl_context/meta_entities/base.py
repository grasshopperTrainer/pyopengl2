import weakref
import abc

import numpy as np

from ckernel.render_context.opengl_context.ogl_entities import OGLEntity
from ckernel.render_context.opengl_context.context_stack import OGLContextStack, OpenglUnboundError
from .error import *


class OGLMetaEntity(metaclass=abc.ABCMeta):
    """
    ! descriptor compatible : read instruction inside __init__
    ! inherit must
    ! abstractmethod:
        `_create_entity`    : method should create an Entity and return

    This class hides concrete context-wise entity, abstracting entity as application dependent not context.
    To work so, it implements factory like functionalities for creating concrete entities in relationship with a
    given(currently bound) OpenGL context.

    ! 'OGLEntity' doesnt mean the class only has to provide OpenGL entity, ex) vao, vbo, ibo.
    It's more like a logical description. 'OGLEntity' describes any object dependent to OGL context.
    """

    @property
    def __context_entity(self):
        """
        lazy parameter assignment

        this removes obligatory super().__init__()
        whilst creating entity storage when needed
        :return:
        """
        name = '__context_entity'
        if not hasattr(self, name):
            setattr(self, name, weakref.WeakKeyDictionary())
        return self.__getattribute__(name)

    def get_concrete(self):
        """
        return correct entity for the context

        Lazy initiating.
        If context is not given, entity of current context will be returned.
        :return: entity for current context
        """
        context = OGLContextStack.get_current()
        if context.is_none:
            raise OpenglUnboundError
        # return if exists already
        if context in self.__context_entity:
            return self.__context_entity[context]
        # if not, create new and store
        with context:
            entity = self._create_entity()
            if not isinstance(entity, OGLEntity):
                raise Exception('creator method is not wrapped, check opengl_hooked')
            self.__context_entity[context] = entity
        return entity

    @abc.abstractmethod
    def _create_entity(self):
        """
        ! internal only : called by self.__get_concrete_entity()

        create new entity for a current context

        Implemented method assuming context is already bound.
        :return: newly created entity
        """

    def __enter__(self):
        """
        connector method, access entity through context manager patter when binding is needed

        :return:
        """
        return self.get_concrete().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        connector method

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        return self.get_concrete().__exit__(exc_type, exc_val, exc_tb)