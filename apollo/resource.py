# Copyright 2023 Apollo API, Inc.
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

from apollo.manager import (
    PostgresConnectionManager,
    FirebaseConnectionManager,
    JSONConnectionManager,
    OpenAIConnectionManager,
)
from apollo.const import QUERY_CONTEXT


class Postgres:

    # Specific sql queries
    _context = QUERY_CONTEXT

    # Database utility class
    _manager = PostgresConnectionManager()

    # curosr instance
    psql_curs = None


class Firebase:
    pass


class JSONService:

    # Service utility class
    _service_manager = JSONConnectionManager()

    # Token
    _auth_token = None


class OpenAI:

    # connection manager
    _openai_manager = OpenAIConnectionManager()

    # model type definition
    _provider_path = None


class General(Postgres, JSONService, OpenAI):

    # Current LLM to be used
    model = None
