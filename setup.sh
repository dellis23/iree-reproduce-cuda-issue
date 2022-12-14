sudo apt install pip
sudo apt install screen
sudo apt install virtualenv
virtualenv venv
source venv/bin/activate
pip install -f https://iree-org.github.io/iree/pip-release-links.html iree-compiler==20221201.344
pip install -f https://iree-org.github.io/iree/pip-release-links.html iree-runtime==20221201.344
pip install -f https://llvm.github.io/torch-mlir/package-index/ torch-mlir==20221201.674
pip install git+https://github.com/iree-org/iree-torch.git
sudo apt-get install linux-headers-$(uname -r)
sudo apt-key del 7fa2af80
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt install cuda
echo 'export PATH=/usr/local/cuda-12.0/bin${PATH:+:${PATH}}' >> ~/.profile
echo 'export PATH=/usr/local/cuda-12.0/bin${PATH:+:${PATH}}' >> venv/bin/activate