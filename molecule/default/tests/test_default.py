"""Role testing files using testinfra."""

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_cache_dir(host):
    """ assert cache dir exists """
    assert host.file('/srv/cache/disk1').exists
    assert host.file('/srv/cache/disk2').exists
