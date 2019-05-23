#!/bin/venv python3
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_is_installed(host):
    pkg = host.package('httpd')
    assert pkg.is_installed


def test_httpd_running_and_enabled(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled


def test_port_80_listening(host):
    port_80 = host.socket("tcp://0.0.0.0:80")
    assert port_80.is_listening
