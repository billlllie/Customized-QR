# Customized-QR






## Content

* [Customized-QR](#customized-qr)
   * [Contents](#contents)
      * [Overview](#overview)
         * [Web QR Code Generator](#web-qr-code-generator)
      * [Install](#install)
         * [To test or debug](#to-test-or-debug)
            * [On Debian](#on-debian)
         * [Setup the website](#setup-the-website)
            * [On Debian](#on-debian-1)
      * [License](#license)



## Overview

### Web QR Code Generator
By the flask framework and guincorn server, the website can process the picture and the QR Code or string that you provided to a customized QR Code.
## Install
You need to install python3, pip(or Setuptools) and [Zbarlight](https://github.com/Polyconseil/zbarlight) to make sure it works.
### To test or debug 

#### On Debian

```
$ sudo apt-get install python3 python3-pip libzbar0 libzbar-dev
$ git clone https://github.com/lzhxwmr/Customized-QR.git
$ cd Customized-QR/
$ pip(3) install -r requirement.txt
$ python3 QR.py
```
It works if you see this:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Actually virtualenv is highly recommended to use.

You can use apt to install virtualenv:

```
$ sudo apt-get install virtualenv
```

Or

```
$ pip(3) install virtualenv
```

And then get into the directory:

```
$ cd Customized-QR/
$ virtualenv -p python3 vnev/
$ pip(3) install -r requirement.txt
$ python3 QR.py
```

### 

### Setup the website

If you want to deploy this project on your server, you should have installed nginx and supervisor.

#### On Debian

```
$ sudo apt-get install nginx supervisor
$ vim conf/QR_nginx.conf
$ vim conf/QR_supervisor.conf
```

Then modify the conf files as you need.

After that, copy this file to nginx directory and make some links:

```
$ cp conf/QR_nginx.conf /etc/nginx/sites-available/
$ ln -S /etc/nginx/sites-available/QR_nginx.conf /etc/nginx/sites-enabled/
$ nginx -s reload
```

You should always `nginx -t` to check if there is anything wrong with your conf file before you  `nginx -s reload` to reload all the configs.

Then configure the supervisor:

```
$ cp conf/QR_supervisor.conf /etc/supervisor/conf.d/
$ supervisorctl reload
```

And now you should be able to visit your site by the domain name you have set.



## License

- GPLv3
