---
name: PDF processing in this workspace
description: Environment-specific setup for visually processing uploaded PDFs.
---

Use the workspace package-management flow to install PyMuPDF, then run PDF scripts with the workspace virtual environment via `uv run`. Direct `pip install` against the system Python is blocked by the immutable Nix environment.

**Why:** Uploaded PDFs are common product inputs, and the system Python does not accept ordinary pip mutations.

**How to apply:** For PDF visual inspection, create the processing script under `.agents/scripts/`, write rendered output under `.agents/outputs/`, and invoke it with `uv run python`.