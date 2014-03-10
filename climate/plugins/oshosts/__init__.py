# Copyright (c) 2014 Bull.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo.config import cfg

RESOURCE_TYPE = u'physical:host'

admin_opts = [
    cfg.StrOpt('climate_username',
               default='climate_admin',
               help='Name of the user for write operations'),
    cfg.StrOpt('climate_password',
               default='climate_password',
               help='Password of the user for write operations'),
    cfg.StrOpt('climate_project_name',
               default='admin',
               help='Project of the user for write operations'),
]

cfg.CONF.register_opts(admin_opts, group=RESOURCE_TYPE)
