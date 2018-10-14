python3 wsgi_app_docker -pp /webapps/examp_user/examp_project -wp /webapps/examp_user/examp_project/examp_project/wsgi.py \
    -rp /webapps/examp_user/examp_project/requirements.txt \
    -pyv 3.6 -sn example.com \
    -an example_app -bp example_app_composedir
