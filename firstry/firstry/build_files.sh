#!/usr/bin/enmv bash
set -e

echo "instalando dependencias"
python3 -m pip install -r requirements.txt
echo "realizando migraciones"
python3 manage.py makemigrations
python3 manage.py migrate

echo "recoplilando archivos estaticos"
python3 manage.py collectstatic --noinput

echo "se completo la configuracion del proyecto"