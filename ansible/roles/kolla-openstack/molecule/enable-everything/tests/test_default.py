# Copyright (c) 2018 StackHPC Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import os.path

from kayobe.tests.molecule import utils

import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    'path',
    ['aodh',
     'barbican',
     'cinder',
     'cloudkitty',
     'designate',
     'fluentd/filter',
     'fluentd/input',
     'fluentd/output',
     'glance',
     'grafana',
     'heat',
     'horizon',
     'ironic',
     'keystone',
     'magnum',
     'manila',
     'mariadb',
     'masakari',
     'murano',
     'neutron',
     'nova',
     'nova/nova-libvirt',
     'octavia',
     'placement',
     'prometheus',
     'sahara',
     'swift'])
def test_service_config_directory(host, path):
    path = os.path.join('/etc/kolla/config', path)
    utils.test_directory(host, path)


@pytest.mark.parametrize(
    'path',
    ['aodh.conf',
     'barbican.conf',
     'cinder.conf',
     'cloudkitty.conf',
     'designate.conf',
     'galera.cnf',
     'glance.conf',
     'grafana.ini',
     'heat.conf',
     'ironic.conf',
     'ironic-inspector.conf',
     'keystone.conf',
     'magnum.conf',
     'manila.conf',
     'masakari.conf',
     'multipath.conf',
     'murano.conf',
     'neutron/ml2_conf.ini',
     'neutron.conf',
     'nova.conf',
     'octavia.conf',
     'placement.conf',
     'sahara.conf',
     'backup.my.cnf'])
def test_service_ini_file(host, path):
    # TODO(mgoddard): Check more of config file contents.
    path = os.path.join('/etc/kolla/config', path)
    extra_section = 'extra-%s' % os.path.basename(path)
    expected = {extra_section: {'foo': 'bar'}}
    utils.test_ini_file(host, path, expected=expected)


@pytest.mark.parametrize(
    'path',
    ['ironic/ironic-agent.initramfs',
     'ironic/ironic-agent.kernel',
     'nova/nova-libvirt/cacert.pem',
     'nova/nova-libvirt/clientcert.pem',
     'nova/nova-libvirt/clientkey.pem'])
def test_service_non_ini_file(host, path):
    # TODO(mgoddard): Check config file contents.
    path = os.path.join('/etc/kolla/config', path)
    utils.test_file(host, path)
