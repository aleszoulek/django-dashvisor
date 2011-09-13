from django.conf import settings
from django.utils.importlib import import_module

def get_backend():
    backend_path = getattr(settings, 'DASHVISOR_BACKEND', 'dashvisor.backends.file.Backend').split('.')
    module_name = ".".join(backend_path[:-1])
    class_name = backend_path[-1]
    backend_module = import_module(module_name)
    return getattr(backend_module, class_name)()

backend = get_backend()
