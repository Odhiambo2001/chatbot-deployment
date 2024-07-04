# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import annotations

from functools import lru_cache
from typing import Literal, Optional

import numpy as np
from numpy.typing import ArrayLike, NDArray

from ..color import get_colormap
from ..gloo import IndexBuffer, VertexBuffer
from ..gloo.texture import should_cast_to_f32
from ..io import load_spatial_filters
from . import Visual
from ._scalable_textures import CPUScaledTexture3D, GPUScaledTextured3D, Texture2D
from .shaders import Function

# todo: implement more render methods (port from visvis)
# todo: allow anisotropic data
# todo: what to do about lighting? ambi/diffuse/spec/shinynes on each visual?

_VERTEX_SHADER: str = ...  # noqa

_FRAGMENT_SHADER: str = ...  # noqa

_RAYCASTING_SETUP_VOLUME: str = ...

_RAYCASTING_SETUP_PLANE: str = ...

_MIP_SNIPPETS = ...

_ATTENUATED_MIP_SNIPPETS = ...

_MINIP_SNIPPETS = ...

_TRANSLUCENT_SNIPPETS = ...

_ADDITIVE_SNIPPETS = ...

_ISO_SNIPPETS = ...

_AVG_SNIPPETS = ...

_INTERPOLATION_TEMPLATE: str = ...

_TEXTURE_LOOKUP: str = ...

class VolumeVisual(Visual):
    _rendering_methods: dict = ...

    _raycasting_modes: dict = ...

    _shaders: dict = ...

    _func_templates: dict = ...

    def __init__(
        self,
        vol: NDArray,
        clim: str | tuple = "auto",
        method: Literal["mip", "attenuated_mip", "minip", "translucent", "additive"] = "mip",
        threshold: float | None = None,
        attenuation: float = 1.0,
        relative_step_size: float = 0.8,
        cmap: str = "grays",
        gamma: float = 1.0,
        interpolation: str = "linear",
        texture_format: np.dtype | None | str = None,
        raycasting_mode: Literal["volume", "plane"] = "volume",
        plane_position: ArrayLike | None = None,
        plane_normal: ArrayLike | None = None,
        plane_thickness: float = 1.0,
        clipping_planes=None,
        clipping_planes_coord_system="scene",
        mip_cutoff=None,
        minip_cutoff=None,
    ): ...
    def _init_interpolation(self, interpolation_methods): ...
    def _create_texture(self, texture_format, data): ...
    def set_data(self, vol: NDArray, clim: tuple | None = None, copy: bool = True): ...
    @property
    def rendering_methods(self): ...
    @property
    def raycasting_modes(self): ...
    @property
    def clim(self): ...
    @clim.setter
    def clim(self, value): ...
    @property
    def gamma(self): ...
    @gamma.setter
    def gamma(self, value): ...
    @property
    def cmap(self): ...
    @cmap.setter
    def cmap(self, cmap): ...
    @property
    def interpolation_methods(self): ...
    @property
    def interpolation(self): ...
    @interpolation.setter
    def interpolation(self, i): ...

    # The interpolation code could be transferred to a dedicated filter
    # function in visuals/filters as discussed in #1051
    def _build_interpolation(self): ...
    @staticmethod
    @lru_cache(maxsize=10)
    def _build_clipping_planes_glsl(n_planes: int) -> str: ...
    @property
    def clipping_planes(self) -> np.ndarray: ...
    @clipping_planes.setter
    def clipping_planes(self, value: Optional[np.ndarray]): ...
    @property
    def clipping_planes_coord_system(self) -> str: ...
    @property
    def _before_loop_snippet(self): ...
    @property
    def _in_loop_snippet(self): ...
    @property
    def _after_loop_snippet(self): ...
    @property
    def method(self): ...
    @method.setter
    def method(self, method): ...
    @property
    def _raycasting_setup_snippet(self): ...
    @property
    def raycasting_mode(self): ...
    @raycasting_mode.setter
    def raycasting_mode(self, value: str): ...
    @property
    def threshold(self): ...
    @threshold.setter
    def threshold(self, value): ...
    @property
    def attenuation(self): ...
    @attenuation.setter
    def attenuation(self, value): ...
    @property
    def relative_step_size(self): ...
    @relative_step_size.setter
    def relative_step_size(self, value): ...
    @property
    def plane_position(self): ...
    @plane_position.setter
    def plane_position(self, value): ...
    @property
    def plane_normal(self): ...
    @plane_normal.setter
    def plane_normal(self, value): ...
    @property
    def plane_thickness(self): ...
    @plane_thickness.setter
    def plane_thickness(self, value: float): ...
    @property
    def mip_cutoff(self): ...
    @mip_cutoff.setter
    def mip_cutoff(self, value): ...
    @property
    def minip_cutoff(self): ...
    @minip_cutoff.setter
    def minip_cutoff(self, value): ...
    def _create_vertex_data(self): ...
    def _compute_bounds(self, axis, view): ...
    def _prepare_transforms(self, view): ...
    def _prepare_draw(self, view): ...
