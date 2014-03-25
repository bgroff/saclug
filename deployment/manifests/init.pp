Exec { path => '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin' }

# Global variables
$inc_file_path = '/vagrant/manifests/files'
$tz = 'US/Pacific'
$project = 'saclug'

include timezone
include apt
include python
include virtualenv
include software

class timezone {
  package { "tzdata":
    ensure => latest,
    require => Class['apt'],
  }

  file { "/etc/localtime":
    require => Package["tzdata"],
    source => "file:///usr/share/zoneinfo/${tz}",
  }
}

class apt {
  exec { 'apt-get update':
    timeout => 0
  }

  package { 'python-software-properties':
    ensure => latest,
    require => Exec['apt-get update'],
  }
}

class python {
  package { 'python':
    ensure => latest,
    require => Class['apt'],
  }

  package { 'python-dev':
    ensure => latest,
    require => Class['apt'],
  }

  package { 'python-pip':
    ensure => latest,
    require => Class['apt'],
  }

}

class virtualenv {
  package { 'virtualenv':
    ensure => latest,
    provider => pip,
    require => Class['python'],
  }

  exec { 'create virtualenv':
    command => "sudo -u vagrant virtualenv /home/vagrant/virtualenv/",
    unless => 'test -d /home/vagrant/virtualenv/',
    require => Package['virtualenv', 'python'],
  }

  exec { 'pip install':
    command => "sudo -u vagrant pip install -E /home/vagrant/virtualenv/ -r /srv/${project}/requirements.txt",
    require => [Exec['create virtualenv'], Class['python']]
  }
}


class software {
  package { 'git':
    ensure => latest,
    require => Class['apt'],
  }

  package { 'zsh':
    ensure => latest,
    require => Class['apt'],
  }
}
