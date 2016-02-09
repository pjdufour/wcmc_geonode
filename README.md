# WCMC Geonode

UNEP-WCMC custom Geonode project template. This repository includes all custom files for UNEP-WCMC implementation of Geonode.

# Installation

## Geonode
Install geonode with::

  ```
  sudo add-apt-repository ppa:geonode/stable
  sudo apt-get update
  sudo apt-get install geonode
  ```

Follow the instructions on Geonode Project's [documentation](https://geonode.readthedocs.org/en/master/tutorials/install_and_admin/index.html)

## Template

### Python Install

On this project's root directory run:

  ```
  sudo pip install -e wcmc_geonode
  ```

### local_settings.py

You  should copy the local_settings.py file to this project. The usual command, from the project's root is:
  ```
  cp /usr/local/lib/python2.7/dist-packages/geonode/local_settings.py /path/to/wcmc_geonode/current/wcmc_geonode/
  ```

The path to the original location of local_settings.py file may differ.

After it, edit its content by setting the SITEURL and SITENAME.


### WSGI setup

Edit the file /etc/apache2/sites-available/geonode.conf and change the following directive from:

  ```
    WSGIScriptAlias / /var/www/geonode/wsgi/geonode.wsgi
  ```

to:

  ```
    WSGIScriptAlias / /path/to/wcmc_geonode/current/wcmc_geonode/wcmc_geonode/wsgi.py
  ```

In the same file add the "Directory" directive for your folder like the following example:

    ```
    <Directory "/path/to/wcmc_geonode/current/wcmc_geonode/wcmc_geonode/">
        Order allow,deny
        Options Indexes FollowSymLinks
        Allow from all
        Require all granted
        IndexOptions FancyIndexing
    </Directory>

    ```

Restart apache::
  ```
  sudo service apache2 restart
  ```

### Collect static files.

After editing the templates you will need to test them on your local installation.

In the wcmc_geonode folder run::
  
  ```
  python manage.py collectstatic
  ```

# Deployment
We are using Capistrano to deploy this project. To use it we recommend using [rvm](https://rvm.io/).

Firstly you should install Ruby 2.2

  ```
  rvm install 2.2
  ```

And under that version install Capistrano

```
gem install capistrano
```

To deploy you should run:

```
cap deploy setup:collectstatic
```