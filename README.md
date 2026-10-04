# PostProject Python host validation

This focused integration consumes only the installed Python package
and native library. It creates a production, imports media, persists a host
reference, and resolves the representation again. See [FINDINGS.md](FINDINGS.md).

The development SDK returns ordinary UUIDs with nominal ID hints. The host
uses `RepresentationRef(id)` when creating its persisted binding; use a
matching SDK wheel and native library.
