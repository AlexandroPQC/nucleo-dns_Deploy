from fabric.api import run, sudo, put, env, task


@task
def install_bind():
	sudo("apt-get -y install bind9")

@task
def deploy_master():
	put("master/named.conf.local", "/etc/bind", use_sudo=True)
	put("master/db.nucleognulinux.com", "/etc/bind", use_sudo=True)
	put("master/db.192.168.1", "/etc/bind", use_sudo=True)
	sudo("service bind9 restart")

@task
def deploy_slave():
	put("slave/named.conf.local", "/etc/bind", use_sudo=True)
	sudo("service bind9 restart")

@task
def deploy_cache():
	put("slave/named.conf.options", "/etc/bind", use_sudo=True)
	sudo("service bind9 restart")

@task
def deploy_simple():
	put("slave/named.conf.local", "/etc/bind", use_sudo=True)
	sudo("service bind9 restart")
@task
def undo_master():
	sudo("service bind9 stop")
	sudo("rm -f /etc/bind/named.conf.local")
	sudo("rm -f /etc/bind/")
	sudo("sed -i '$d' /etc/hosts")
