## WIP


## Version 0.1: start of assignment

* First code.
Added to .toml file to specify which files to include in wheel. This fixed warnings I was having
with nox -s tests or docs

$ [tool.hatch.build.targets.wheel]
$ packages = ["src/unc"]
-----------------------------
Second Commit
I had several warnings in tests (3.9) and tests (3.13), I did this to address:
added installing nox to the install dependencies in ci.yml
changed pre-commit diff command to git diff in the Run pre-commit section

------------------------------------
Third Commit
I had several warings in the pre-commit check that were automatically identified. Some were changed automatically, these ones werent:
changed δC to deltaC in __init__.py
removed the unused import TypeVar
added this to pyproject.toml to remove deprecation warning:
[tool.ruff.lint.per-file-ignores]
"tests/**" = ["T20"]
