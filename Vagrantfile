# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "trusty64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network "private_network", ip: "10.10.10.33"

  # Share the salt config with the guest
  config.vm.synced_folder "salt", "/srv/salt/"
  config.vm.synced_folder "pillar", "/srv/pillar"

  ## Use all the defaults:
  config.vm.provision :salt do |salt|

    salt.minion_config = "salt/vagrant-minion"
    salt.run_highstate = true
    salt.verbose = true
    salt.install_type = "-P git"
    salt.install_args = "v2015.5.5"
  end
end
