import os
from unittest import mock
from instarest.core.config import (
    EnvironmentSettings,
    CoreSettings,
    get_core_settings,
    get_environment_settings,
)

BASEDIR = os.path.join(
    os.path.abspath(os.path.dirname("./instarest/core/config.py")), "env_var"
)


def test_settings_exists():
    assert isinstance(get_core_settings(), CoreSettings)
    assert isinstance(get_environment_settings(), EnvironmentSettings)


@mock.patch.dict(
    os.environ, clear=True
)  # clear=True is needed to clear the environment variables
def test_example_app_default():
    environment_settings = EnvironmentSettings()
    assert environment_settings.environment == "local"


@mock.patch.dict(os.environ, {"SECRETS": "True"})
def test_secrets_are_searched():
    environment_settings = EnvironmentSettings()

    try:
        environment_settings.pull_settings()
    except FileNotFoundError:
        assert True
        return

    assert False


@mock.patch.dict(os.environ, {"ENVIRONMENT": "development"})
def test_env_file_name_development():
    environment_settings = EnvironmentSettings()
    core_settings = environment_settings.pull_settings()
    assert core_settings.postgres_password == "fake-development"


@mock.patch.dict(os.environ, {"ENVIRONMENT": "local"})
def test_env_file_name_local():
    environment_settings = EnvironmentSettings()
    core_settings = environment_settings.pull_settings()
    assert core_settings.postgres_password == "postgres"


@mock.patch.dict(os.environ, {"ENVIRONMENT": "production"})
def test_env_file_name_production():
    environment_settings = EnvironmentSettings()
    core_settings = environment_settings.pull_settings()
    assert core_settings.postgres_password == "fake-production"


@mock.patch.dict(os.environ, {"ENVIRONMENT": "staging"})
def test_env_file_name_staging():
    environment_settings = EnvironmentSettings()
    core_settings = environment_settings.pull_settings()
    assert core_settings.postgres_password == "fake-staging"


@mock.patch.dict(os.environ, {"ENVIRONMENT": "test"})
def test_env_file_name_test():
    environment_settings = EnvironmentSettings()
    core_settings = environment_settings.pull_settings()
    assert core_settings.postgres_password == "fake-test"
