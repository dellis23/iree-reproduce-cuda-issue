# iree-reproduce-cuda-issue

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