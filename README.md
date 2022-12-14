# iree-reproduce-cuda-issue

## Environment Setup

The following was run on a GCP n1-standard-4 Intel Haswell x86/64 instance
with an NVIDIA T4 GPU on Ubuntu 22.04.

## Running the Repro

First, run the setup script, saying Y at all prompts.

```
./setup.sh
```

Then, reboot:

```
sudo reboot
```

Then, activate the virtual environment and run the test script:

```
source venv/bin/activate
python model-test.py
```