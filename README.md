# translator3
Python is completely unsuitable for ransomware but I wanted to give it a go anyway. This is only a proof of concept and hasn't been properly tested. Modify `real_ransomware.py` to suit your needs (create a new RSA key pair and replace the public key and change the email address), then execute `python3 generate3.py real_ransomware.py` to generate a new `translator3.py`. All dependencies for `translator3.py` are included (and pure Python only, so entirely cross platform), but if the `cryptography` (`python3 -m pip install cryptography`) module is found on the victim's computer, it will be used instead for improved performance.

translator3 is supposed to be compatible with any Linux distro, MacOS and Windows. On MacOS and Linux, translator3 becomes a daemon by forking twice. This does not work on Windows and I am yet to figure out how to daemonise (or become a "service") in Windows. It has been tested on a Fedora 36 virtual machine and a MacOS virtual machine (not on Apple hardware, so it may be different on an actual Mac?). I have only tested it with CPython 3.10.7.

Please do not use this to cause harm to others. It is only intended for experimentation and as a proof of concept for a ransomware written in Python. I am not responsible for any damage caused by this program.

The ransomware is base64 encoded and then encoded into various zero width/invisible characters. translator3 then decodes it and executes it.

## Performance
Using the included, pure Python AES implementation, I have observed encryption speeds of about 35kb/s (I know, it's terrible) on bare metal (2x1.5GHz cores, 16GB RAM, eMMC) and about 20kb/s in a virtual machine (2x1.5GHz cores, 8GB RAM, SSD). Using the `cryptography` module, I have observed speeds of many hundereds of megabytes per second. I have not tested decryption speeds or pure Python RSA speeds, but that is insignificant as the RSA module is only used to encrypt the 256bit AES encryption key, not the actual files.

## generate3 usage
```
python3 generate3.py [payload file path] <options>
```
### Options
```
--newline=<newline>  Add a new line to the encoded payload every <newline> characters
--no-ettt            "no enter text to translate" - do not prompt the user to enter text to translate
--name=<name>        The name of the directory to create `translator3.py` in
```

# License
The translator3 Project is licensed under the GPLv3 (or newer) license. See the LICENSE file for more information.
Copyright (c) 2022 Benjamin Mickler