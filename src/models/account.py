import enum
import json
from typing import Optional, cast

from flask_login import UserMixin  # type: ignore
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, reconstructor

from models.base import Base

from .engine import db
from .types import StringUUID


class Tenant(Base):
    __tablename__ = "tenants"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="tenant_pkey"),)

    id = db.Column(StringUUID, server_default=db.text("uuid_generate_v4()"))
    name = db.Column(db.String(255), nullable=False)
    encrypt_public_key = db.Column(db.Text)
    plan = db.Column(
        db.String(255),
        nullable=False,
        server_default=db.text("'basic'::character varying"),
    )
    status = db.Column(
        db.String(255),
        nullable=False,
        server_default=db.text("'normal'::character varying"),
    )
    custom_config = db.Column(db.Text)
    created_at = db.Column(
        db.DateTime, nullable=False, server_default=func.current_timestamp()
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, server_default=func.current_timestamp()
    )

    # def get_accounts(self) -> list[Account]:
    #     return (
    #         db.session.query(Account)
    #         .filter(Account.id == TenantAccountJoin.account_id, TenantAccountJoin.tenant_id == self.id)
    #         .all()
    #     )

    @property
    def custom_config_dict(self) -> dict:
        return json.loads(self.custom_config) if self.custom_config else {}

    @custom_config_dict.setter
    def custom_config_dict(self, value: dict):
        self.custom_config = json.dumps(value)
