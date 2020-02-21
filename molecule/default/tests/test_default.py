import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_squid(host):
    pkg = host.package('squid')
    port = host.socket('tcp://0.0.0.0:3128')

    assert pkg.is_installed
    assert port.is_listening


def test_cache_dir(host):
    assert host.file('/srv/cache/disk1').exists
    assert host.file('/srv/cache/disk2').exists

    host_type = host.system_info.distribution
    file = host.file('/srv/cache/disk1')

    if(host_type == 'centos'):
        assert file.user == 'squid'
        assert file.group == 'squid'
    else:
        assert file.user == 'proxy'
        assert file.group == 'proxy'
