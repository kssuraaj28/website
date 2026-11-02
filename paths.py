import re
from dataclasses import dataclass


# Just a generic path mechanism
# A sequence of validated URL path segments.
# You can use this for a lot of places, like basename, absolute paths, relative paths, etc.
@dataclass(frozen=True)
class SanitizedPath:
    content: tuple[str, ...]

    def __post_init__(self):
        for seg in self.content:
            # Heavy sanitization
            if not re.fullmatch(r"[a-z0-9._-]+", seg) or seg in (".", ".."):
                # !r calls repr instead
                raise ValueError(f"Invalid path segment: {seg!r}")


def join(p1: SanitizedPath, p2: SanitizedPath) -> SanitizedPath:
    return SanitizedPath(p1.content + p2.content)
