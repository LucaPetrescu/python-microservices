from . import validate as _validate
import sys

# Make validate available in the auth namespace
sys.modules['auth.validate'] = _validate
validate = _validate
