namespace :translation do
  desc "Collects static files"
  task :update do
	  system "sudo cp translations/en/django.po /usr/local/lib/python2.7/dist-packages/geonode/locale/en/LC_MESSAGES/"
    system "cd /usr/local/lib/python2.7/dist-packages/geonode/ && sudo django-admin.py compilemessages -l en"
    system "python ~/wcmc_geonode/wcmc_geonode/manage.py collectstatic --noinput"
    system "sudo service apache2 restart"
  end
end