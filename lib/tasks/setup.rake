namespace :setup do
  desc "Collects static files"
  task :collectstatic do
    on roles(:web) do
	    execute "sudo cp ~/wcmc_geonode/current/translations/en/django.po /usr/local/lib/python2.7/dist-packages/geonode/locale/en/LC_MESSAGES/"
      execute "cd /usr/local/lib/python2.7/dist-packages/geonode/ && sudo django-admin.py compilemessages -l en"
      execute "cd ~/wcmc_geonode/current && sudo pip install -e wcmc_geonode && cp /etc/geonode/local_settings.py ~/wcmc_geonode/current/wcmc_geonode/"
      execute "python ~/wcmc_geonode/current/wcmc_geonode/manage.py collectstatic --noinput"
      execute "sudo service apache2 restart"
    end
  end
end
