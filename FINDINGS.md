# Findings

- The Python binding can remain an ordinary host dependency; no Rust type or
  build step appears in host code.
- Keyed collections (`production.representations[asset_id]`) are concise, but a
  new user needs one example before their shape is obvious.
- Host-object bindings remove the temptation to persist a filesystem path or a
  bare UUID in application state.
- Explicit transaction scope and immutable result snapshots fit host task
  boundaries cleanly.

