namespace :setup do
  desc "Collects static files"
  task :collectstatic do
    on roles(:web) do
      execute "python /home/ubuntu/wcmc_geonode/current/manage.py collectstatic --noinput"
    end
  end
end
