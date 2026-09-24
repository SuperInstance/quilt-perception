"""quilt-perception — Perception substrate — routes sensor data through 6 perception slots.

Brewed by quilt-brewer from recipe 'quilt-perception'.

Polarity rules:
  - ACCEPT: ok
  - DRIFT: warn
  - REFUSE: fail
"""
from .sensor_stream import SensorStreamSubstrate

__version__ = "0.1.0"
__all__ = ["SensorStreamSubstrate"]
