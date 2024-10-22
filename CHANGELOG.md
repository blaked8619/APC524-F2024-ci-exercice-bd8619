## WIP


## Version 0.1: start of assignment

* First code.
------------------------------
Added to .toml file to specify which files to include in wheel. This fixed warnings I was having
with nox -s tests or docs

$ [tool.hatch.build.targets.wheel]
$ packages = ["src/unc"]
-----------------------------
Second Commit
added installing nox to the install dependencies in ci.yml
changed pre-commit diff command to git diff in the Run pre-commit section



