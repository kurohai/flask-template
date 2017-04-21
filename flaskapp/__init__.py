#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kurohai
# @Date:   2015-11-18 21:47:31
# @Last Modified by:   evan
# @Last Modified time: 2015-12-16 12:14:11


from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table
from sqlalchemy.pool import QueuePool, SingletonThreadPool
from sqlalchemy.ext.declarative import *
from flask import Flask
import datetime
import os
from dicto import dicto
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import DevelopmentConfig, TestingConfig, ProductionConfig, StagingConfig

settings = DevelopmentConfig()

@as_declarative()
class BaseBase(dicto):

    def __hash__(self):
        return hash(self.id)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = BaseBase

engine = create_engine(settings.dburi)
metadata = MetaData(bind=engine)
session = Session(engine)
db_session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine
    )
)

Base.metadata = metadata
Base.query = db_session.query_property()


from models import User, Log
from app import flasktemplate
from forms import LoginForm, SearchForm
from views import blueprint
from log_view import log_blueprint


flasktemplate.register_blueprint(blueprint)
if settings.logging:
    flasktemplate.register_blueprint(log_blueprint)
