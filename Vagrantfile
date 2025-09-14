Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  # VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 2
  end

  # Forward guest port 5000 -> host port 5001
  config.vm.network "forwarded_port", guest: 5000, host: 5001

  # Provisioning script: install Python, dependencies, DB, and run gunicorn
  config.vm.provision "shell", inline: <<-SHELL
    set -eux

    # Update and install essentials
    apt-get update
    apt-get install -y python3 python3-venv python3-pip git build-essential

    # Navigate to synced folder
    cd /vagrant

    # Create virtual environment and activate it
    python3 -m venv venv
    . venv/bin/activate

    # Upgrade pip and install Python dependencies
    pip install --upgrade pip
    pip install -r requirements.txt

    # Initialize DB (if using SQLite or SQLAlchemy)
    python init_db.py || true

    # Kill any previous gunicorn processes
    pkill -f gunicorn || true

    # Launch gunicorn detached; logs written to /vagrant/gunicorn.log
    nohup venv/bin/gunicorn -b 0.0.0.0:5000 hangman:app --workers 2 > /vagrant/gunicorn.log 2>&1 &
  SHELL
end
