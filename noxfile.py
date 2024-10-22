import nox

@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "--serve" to serve.
    """

    session.install(".[docs]")
    session.chdir("docs")
    session.run("sphinx-build", "-M", "html", ".", "build")

@nox.session
def tests(session: nox.Session) -> None:
    """
    Run tests.
    """
    session.install(".[test]")
    session.run("pytest")
