from examples.example_app import DeclarativeBase


def test_env_var_defined_db_schema_name(db):
    assert DeclarativeBase.metadata.schema == "public"
