from sqlalchemy import select

from fastapi_curso.models import User


def test_create_user(session):
    user = User(
        username='Paula',
        userpassword='secret@123',
        usermail='paula@gmail.com',
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.usermail == 'paula@gmail.com')
    )
    assert result.id == 1
