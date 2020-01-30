from io import BytesIO
import inspect
import numpy as np
from PIL import Image

def trim_call(f, /, **kwargs):
    sig = inspect.signature(f).parameters
    return f(**{k: v for k, v in kwargs.items() if k in sig})

# Transformations for our drawable objects
class MetaDrawable(type):
    def __new__(cls, name, bases, namespace):
        namespace['stack'] = {}

        try:
            draw = namespace['Draw']
        except KeyError:
            pass
        else:
            namespace['stack'] = {i: getattr(draw, i) for i in vars(draw) if not i.startswith('_')}

        return type.__new__(cls, name, bases, namespace)

# Class of all drawable objects
# You will never want to inherit this object directly, please use Scene instead
class Drawable(metaclass=MetaDrawable):
    def __init__(self, **kwargs):
        def add_to_stack(k, v):
            self.stack[k] = v

        [add_to_stack(k, v) for k, v in kwargs.items()]

    def _build(self):
        result = {}

        def resolve_dependencies(element):
            try:
                return trim_call(element, **result)

            except TypeError:
                return element

        for k, v in self.stack.items():
            result[k] = resolve_dependencies(v)
        return result


    def __repr__(self):
        built = self._build()
        params = ','.join(f"{k}={v}" for k, v in built.items())
        return f"{self.__class__.__name__}({params})"

    def _repr_png_(self):
        result = self.draw()
        result[result == None] = 0
        with BytesIO() as out:
            Image.fromarray(result.astype(np.uint8)).save(out, format='png')
            out.seek(0)
            return out.read()

    def draw(self):
        built = self._build()
        out = np.full((100, 100), None)
        for i in built:
            try:
                new_draw = i.draw()
                out = np.where(new_draw != None, new_draw, out)
            except AttributeError:
                pass

        return out
