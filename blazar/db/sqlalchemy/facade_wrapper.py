# Copyright 2014 Intel Corporation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg
from oslo_db.sqlalchemy import session as db_session


CONF = cfg.CONF

_engine_facade = None


def get_session():
    return _get_facade().get_session()


def get_engine():
    return _get_facade().get_engine()


def _clear_engine():
    global _engine_facade
    _engine_facade = None


def _get_facade():
    global _engine_facade
    if not _engine_facade:
        # FIXME(priteau): Remove autocommit=True (and ideally use of
        # LegacyEngineFacade) asap since it's not compatible with SQLAlchemy
        # 2.0.
        _engine_facade = db_session.EngineFacade.from_config(CONF,
                                                             autocommit=True)

    return _engine_facade
