import logging
from threaded import Threaded
from functools import wraps
from common import configure_logging, runit

logger = logging.getLogger(__name__)

configure_logging()

threaded = Threaded(workers=5)

def register(**kwargs):
    def decorator(function):   
        threaded.register(function, **kwargs)
        @wraps(function)
        def wrapper(**kwargs):
            return function(**kwargs)
        return wrapper
    return decorator

@register()
def i01():
    runit(i01.__name__)

@register()
def i02():
    runit(i02.__name__)

@register()
def i03():
    runit(i03.__name__)

@register()
def i04():
    runit(i04.__name__)

@register(after=['i01'])
def i05():
    runit(i05.__name__)

@register(after=['i01'])
def i06():
    runit(i06.__name__)

@register(after=['i01'])
def i07():
    runit(i07.__name__)

@register(after=['i01'])
def i08():
    runit(i08.__name__)

@register(after=['i04'])
def i09():
    runit(i09.__name__)

@register(after=['i04'])
def i10():
    runit(i10.__name__)

@register(after=['i04'])
def i11():
    runit(i11.__name__)

@register(after=['i06'])
def i12():
    runit(i12.__name__)

@register(after=['i06'])
def i13():
    runit(i13.__name__)

@register(after=['i06'])
def i14():
    runit(i14.__name__)

@register(after=['i09'])
def i15():
    runit(i15.__name__)

@register(after=['i12'])
def i16():
    runit(i16.__name__)

@register(after=['i16'])
def i17():
    runit(i17.__name__)

if __name__ == '__main__':
    threaded.start()
