from distutils.core import setup

setup(
    name="m5-jenkins-python",
    version="1.0",
    py_modules=["src/app"],
    install_requires=["flask", "django"]
)
