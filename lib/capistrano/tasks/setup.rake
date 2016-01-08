namespace :setup do
  desc "Collects static files"
  task :collectstatic do
    on roles(:web) do
      execute "python /home/ubuntu/wcmc_geonode/current/wcmc_geonode/manage.py collectstatic --noinput"
    end
  end

  task :update_translation do
    on roles(:web) do
      execute "sudo cp ~/wcmc_geonode/current/translations/en/django.po /usr/local/lib/python2.7/dist-packages/geonode/locale/en/LC_MESSAGES/"
      execute "cd /usr/local/lib/python2.7/dist-packages/geonode/ && sudo django-admin.py compilemessages -l en && sudo apache2 restart"
    end
  end
end
