from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("django-generic-contact")
except PackageNotFoundError:  # pragma: no cover - fallback for editable installs
    __version__ = "0.0.0"
