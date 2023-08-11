from .context import ProxyManager

def get_proxy_path():
    import os
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'proxies.txt')
    return filepath

def test_load_proxies():
    proxy_manager = ProxyManager(get_proxy_path())
    assert len(proxy_manager.proxies) == 2

def test_next_proxy():
    proxy_manager = ProxyManager(get_proxy_path())
    assert proxy_manager.next_proxy().proxy_string == '00.11.222.33:4444'

def test_auth_proxy():
    proxy_manager = ProxyManager(get_proxy_path())
    assert proxy_manager.proxies[1].proxy_string == 'username:password@55.66.777.88:9999'

def test_proxy_dict():
    proxy_manager = ProxyManager(get_proxy_path())
    assert proxy_manager.proxies[0].get_dict() == {'http': 'http://00.11.222.33:4444', 'https': 'https://00.11.222.33:4444'}

def test_no_proxies():
    proxy_manager = ProxyManager(proxy_file_path=None)
    assert len(proxy_manager.proxies) == 1
    assert proxy_manager.proxies[0].get_dict() == {}
