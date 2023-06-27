from setuptools import setup, find_packages

setup(
    name="ci-secrets-cli",
    version="0.0.1",
    author="Aleksandr Kiriushin",
    author_email="aleksandr.kiriushin@klarna.com",
    description="Placeholder in public PyPi to shadow internal ci-secrets-cli package",
    url="https://github.com/aleksandr-kiriushin-klarna/ci-secrets-cli",
    packages=find_packages(),
    python_requires='>=3.8',
)
