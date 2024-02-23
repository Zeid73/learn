from dynaconf import Dynaconf, Validator

db_settings = Dynaconf(
    settings_files=["./libs_ex/db_config.toml"],
    envvar_prefix="DYNACONF",
    environments=True,
    env_switcher="ENV_FOR_DYNACONF",
    default_env="mysql",
    env="mysql",
)

db_settings.validators.register(
    Validator("db", must_exist=True),
    Validator("root.username", must_exist=True, env="mysql"),
    Validator(
        "root.password",
        must_exist=True,
        when=Validator("root.username", must_exist=True),
    ),
    Validator("username", must_exist=True, env="z"),
    # Validator("mysql.admin.username", must_exist=True),
    # Validator("mysql.admin.password", must_exist=True),
    # Validator("mysql.builder.username", must_exist=True),
    # Validator("mysql.builder.password", must_exist=True),
    # Validator("mysql.writer.username", must_exist=True),
    # Validator("mysql.writer.password", must_exist=True),
    # Validator("mysql.reader.username", must_exist=True),
    # Validator("mysql.reader.password", must_exist=True),
)

db_settings.validators.validate()

# from libs_ex.db_config import db_settings

# # with db_settings.using_env("mysql"):
# print(db_settings.db)
# print(db_settings.root.username)

with db_settings.using_env("z"):
    print(db_settings.username)
    print(db_settings.root.password)
