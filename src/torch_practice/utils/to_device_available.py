"""Utilities."""

import logging

import torch
from torch import nn

logger = logging.getLogger(__name__)


def to_device_available(net: nn.Module) -> str:
  """Send to device (GPU/MPS) if available.

  Returns
  -------
    device: where it was sent to.

  """
  device = "cpu"
  if torch.cuda.is_available():
    device = "cuda"
    if torch.cuda.device_count() > 1:
      logger.info("Trying GPU in parallel.")
      net = nn.DataParallel(net)
  elif torch.mps.is_available():
    device = "mps"
  net = net.to(device)
  return device