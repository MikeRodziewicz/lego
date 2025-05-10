"""
Configuration module for the tests. 

"""
from collections.abc import Generator

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import Engine, StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from main.app import Base, app
from main.core.database import get_db_session
from main.models.base import Base

DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(name="test_client")
def fx_test_client(
    fx_session_factory
) -> Generator[TestClient, None, None]:
    test_client = TestClient(app)
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides[get_db_session] = fx_session_factory 

@pytest.fixture(scope="session", name="get_test_db")
def fx_override_get_db() -> Generator[Engine, None, None]:
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "check_same_thread": False,
        },
        poolclass=StaticPool,
    )
    yield engine

@pytest.fixture(scope="session")
def fx_session_factory(get_test_db: Engine) -> sessionmaker:
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_test_db, expire_on_commit=False)
    return TestingSessionLocal

@pytest.fixture(scope="function")
def fx_test_get_db_session(
    fx_session_factory: sessionmaker
) -> Generator[Session, None, None]:
    """This yields a separate session when needed."""
    with fx_session_factory(autobegin=False) as session:
        yield session

@pytest.fixture(name="db_setup_teardown")
def fx_db_setup_teardown(get_test_db: Engine) -> Generator[None, None, None]:
    Base.metadata.create_all(bind=get_test_db)
    yield
    Base.metadata.drop_all(bind=get_test_db)

